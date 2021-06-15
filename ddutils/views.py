# coding: utf-8

from django.views.generic import ListView, DetailView
from django.shortcuts import render, get_object_or_404
from django.http.response import JsonResponse

from .utils import DDPagination
from .mixins import LoginRequiredMixin, MessageMixin, SerializerMixin


class DDListView(ListView, LoginRequiredMixin, MessageMixin, SerializerMixin):

    queryset = None
    model = None
    pagination_class = DDPagination
    serializer_fields = ()

    def get(self, request, *args, **kwargs):
        pagination = self.pagination_class(request, self.get_queryset(request)).pagination()
        message = self.get_messages()
        context = self.get_context_data(request, *args, **kwargs)
        context.update(message)
        context.update(pagination)
        if request.is_ajax():
            if self.serializer_fields and pagination.get('result', []):
                data = self.searializer_data(pagination)
                return JsonResponse(data)
            return JsonResponse({'total': 0, 'result': [], 'count': 0})

        return render(request, self.template_name, context=context)

    def get_context_data(self, request, *args, **kwargs):
        return {}

    def get_queryset(self, request):
        return self.queryset


class DDDetailView(DetailView, MessageMixin, SerializerMixin):

    model = None

    def get(self, request, pk):
        object = self.get_object(pk)
        context = self.get_context_data(request, pk)
        if request.is_ajax():
            data = {'result': [object]}
            if self.serializer_fields and data.get('result', []):
                data = self.searializer_data(data)
                return JsonResponse(data)
            return JsonResponse(context)
        context.update({'object': object})
        return render(request, self.template_name, context=context)

    def get_object(self, queryset=None):
        return get_object_or_404(self.model, pk=queryset)

    def get_context_data(self, request, pk):
        return {}