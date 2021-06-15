# coding: utf-8

from django.db.models import Q
from django.conf import settings
from django.shortcuts import get_object_or_404

from .models import Task, Category, TaskLog, TaskConf, TaskInputParams
from ddutils.views import DDListView, DDDetailView


class TaskListView(DDListView):
    model = Task
    queryset = Task.objects.all()
    template_name = "jobs/task_list.html"
    serializer_fields = ('name', 'type', 'category', 'id')

    def get_context_data(self, request, *args, **kwargs):
        categories = [category for category in Category.objects.all()]
        types = ['shell', 'playbook']
        return {'categories': categories, 'types': types}

    def searializer_data(self, pagination):
        tasks = []
        for task in pagination['result']:
            category = Category.objects.get(id=task.category)
            task.category = category.display
            tasks.append(task)
        pagination['result'] = tasks
        return super(TaskListView, self).searializer_data(pagination)

    def get_queryset(self, request):
        queryset = self.queryset
        type = request.GET.get('type', None)
        name = request.GET.get('name', None)
        category = request.GET.get('category', None)

        if category:
            try:
                category = Category.objects.get(name=category)
            except Category.DoesNotExist:
                category = None
            if category:
                queryset = queryset.filter(category=category.id)
        if type in settings.TASK_TYPES.values():
            queryset = queryset.filter(type=type)

        if name:
            queryset = queryset.filter(Q(name__contains=name))

        return queryset.all()


class TaskDetailView(DDDetailView):
    model = Task
    template_name = "jobs/task_detail.html"


class TaskEditView(DDDetailView):
    model = Task
    template_name = "jobs/task_edit.html"

    def get_context_data(self, request, pk):
        task_conf = TaskConf.objects.filter(task_id=pk).first()
        if not task_conf:
            task_conf = TaskConf(task_id=pk)
            task_conf.save()
        return {'conf': task_conf}


class TaskLogListView(DDListView):
    model = TaskLog
    queryset = TaskLog.objects.all()

    def get_queryset(self, request):
        task_id = request.GET.get('task_id', 0)
        return self.queryset.filter(task_id=task_id).all()
