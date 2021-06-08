# coding: utf-8

from django.db.models import Q
from django.conf import settings

from .models import Task, Category
from ddutils.views import DDListView


class TaskListView(DDListView):
    model = Task
    queryset = Task.objects.all()
    template_name = "jobs/task_list.html"
    serializer_fields = ('name', 'type', 'category')

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


class CategoryListView(DDListView):
    model = Category
