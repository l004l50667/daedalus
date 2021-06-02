# coding: utf-8

from django.core.paginator import Paginator
from django.core.paginator import PageNotAnInteger
from django.core.paginator import EmptyPage


class DDPagination(object):
    '''
        {
            'page': 当前第几页,
            'total': 一共多少项
            'size': 一页多少个
            result: 返回时的实例对象
        }
    '''
    page_size = 10
    page_kwarg = 'page'
    page_size_kwarg = 'size'

    def __init__(self, request, queryset):
        self.request = request
        self.paginator = Paginator(queryset, self.size)
        print self.size

    def pagination(self):
        return {'page': self.page, 'size': self.size, 'total': self.total, 'result': self.result}

    @property
    def result(self):
        try:
            page = self.paginator.page(self.page)
        except PageNotAnInteger:
            page = self.paginator.page(1)
        except EmptyPage:
            page = self.paginator.page(self.paginator.num_pages)
        return page.object_list

    @property
    def total(self):
        return self.paginator.count

    @property
    def page(self):
        return self.request.GET.get(self.page_kwarg, 1)

    @property
    def size(self):
        return self.request.GET.get(self.page_size_kwarg, self.page_size)
