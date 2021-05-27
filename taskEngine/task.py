# coding: utf-8

import os

from django.conf import settings

from taskEngine.celery import app
from tasks.models import Category, Task


@app.task
def scan_tasks():
    '''
    扫描任务：
        从tasks目录下扫描文件, 入库
        ${tasks}/${category}/${type}/${task_file}
        ${tasks}/common/app1/test.sh
        映射到task的model
            name: app1_test
            task_type: shell
            category: common    #common 需要事先在分类表中定义
            path: common/app1/test.sh

    步骤:
        1. 扫描任务目录
        2. 如果任务不再数据库中则进行处理
            0) 获取到任务路径
            1) 根据路径获取到分类信息, 确认分类存在，获取到分类的id保存数据库
            2) 获取到任务名称
            3）创建任务实例保存数据库
            4) 任务实例创建完成还需要前端去设置一些配置信息:
                参数设置
                执行用户设置
                超时时间
    :return:
    '''
    result = {}
    for category in os.listdir(settings.TASKS_PATH):
        category = CategoryTask(category)
        if not category.is_validate():
            continue
        ret = category.scan()
        if ret:
            result[category.name] = u'Scan {} Success'.format(category.name)
        else:
            result[category.name] = u'Scan {} Failed'.format(category.name)
    return result


def get_name_type(file_name):
    try:
        task_name, task_type = file_name.split('.')
        if task_type in settings.TASK_TYPES.keys():
            return task_name, settings.TASK_TYPES[task_type]
        return None, None
    except:
        return None, None


def get_dirs_files(path):
    if not os.path.exists(path):
        return [], []

    dirs, files = [], []
    for item in os.listdir(path):
        item_path = os.path.join(path, item)
        if os.path.isfile(item_path):
            files.append(item)
        if os.path.isdir(item_path):
            dirs.append(item)
    return dirs, files


class CategoryTask(object):

    def __init__(self, name):
        self.name = name
        self.path = os.path.join(settings.TASKS_PATH, name)
        self.category = Category.objects.get(name=name)
        self.tasks = []
        self.tasks_ids = []

    def scan_tasks(self):
        '''
        扫描返回数据库中部存在的任务
        :return:
        '''
        tasks = self.list_tasks()
        if not tasks:
            return []
        for task_name, task_type, path in tasks:
            task = Task.objects.filter(name=task_name).filter(category=self.category.id).first()
            if task:
                continue
            self.tasks.append((task_name, task_type, path ))
        return self.tasks

    def save_tasks(self):
        for task_name, task_type, path in self.tasks:
            task = Task.objects.filter(name=task_name).filter(category=self.category.id).first()
            if task:
                continue
            task = Task(name=task_name, category=self.category.id, path=path)
            task.save()
            self.tasks_ids.append(task.id)

    def list_tasks(self):
        tasks = []
        dirs, files = get_dirs_files(self.path)
        # 将文件都扫描加到当前分类的任务下
        for item in files:
            task_name, task_type = get_name_type(item)
            if not task_name or not task_type:
                continue
            path = os.path.join(self.path, item)
            tasks.append((task_name, task_type, path))
        # 将目录都扫描进来, 目录只支持一级
        for item in dirs:
            dirs, files = get_dirs_files(os.path.join(self.path, item))
            for f in files:
                task_name, task_type = get_name_type(f)
                if not task_name or not task_type:
                    continue
                path = os.path.join(self.path, item, f)
                tasks.append(('{}_{}'.format(item, task_name), task_type, path))
        return tasks

    def is_validate(self):
        return self.category is not None

    def scan(self):
        tasks = self.scan_tasks()
        if not tasks:
            return True
        self.save_tasks()
        if len(self.tasks) == len(self.tasks_ids):
            return True
        return False
