# coding: utf-8
from django.shortcuts import render
from django.views.generic import ListView

from .models import Task, Category
from ddutils.views import DDListView


class TaskListView(DDListView):
    model = Task
    queryset = Task.objects.all()
    template_name = "jobs/task_list.html"


class CategoryListView(DDListView):
    model = Category
