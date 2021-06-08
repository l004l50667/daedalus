# coding: utf-8

from django.views.generic import ListView
from django.shortcuts import render
from django.http.response import JsonResponse

from .utils import DDPagination
from .mixins import LoginRequiredMixin


class DDListView(ListView, LoginRequiredMixin):

    queryset = None
    model = None
    pagination_class = DDPagination
    serializer_fields = ()

    def get_messages(self):
        return {}

    def get(self, request, *args, **kwargs):
        pagination = self.pagination_class(request, self.get_queryset(request)).pagination()
        message = self.get_messages()
        context = self.get_context_data(request, *args, **kwargs)
        context.update(message)
        context.update(pagination)
        if request.is_ajax():
            print 'is ajax ====================='
            if self.serializer_fields and pagination.get('result', []):
                print 'is ajax serializer data'
                data = self.searializer_data(pagination)
                return JsonResponse(data)

        print 'template response'
        return render(request, self.template_name, context=context)

    def get_context_data(self, request, *args, **kwargs):
        return {}

    def get_queryset(self, request):
        return self.queryset

    def searializer_data(self, pagination):
        pagination['result'] = [
            { field: getattr(obj, field) for field in self.serializer_fields}
            for obj in pagination['result']
        ]
        return pagination