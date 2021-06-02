# coding: utf-8

from django.views.generic import ListView
from django.shortcuts import render

from .utils import DDPagination
from .mixins import LoginRequiredMixin


class DDListView(ListView, LoginRequiredMixin):

    queryset = None
    model = None
    pagination_class = DDPagination

    def get_messages(self):
        return {}

    def get(self, request, *args, **kwargs):
        pagination = self.pagination_class(request, self.queryset).pagination()
        message = self.get_messages()
        context = self.get_context_data(request, *args, **kwargs)
        context.update(message)
        context.update(pagination)
        print context
        return render(request, self.template_name, context=context)

    def get_context_data(self, request, *args, **kwargs):
        return {}
