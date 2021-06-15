# coding: utf-8


from django.http import Http404
from django.shortcuts import render

from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required


class LoginRequiredMixin(object):

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super(LoginRequiredMixin, self).dispatch(request,*args, **kwargs)


class MessageMixin(object):

    def get_messages(self):
        return {}


class SerializerMixin(object):

    serializer_fields = ()

    def searializer_data(self, pagination):
        pagination['result'] = [
            { field: getattr(obj, field) for field in self.serializer_fields}
            for obj in pagination['result']
        ]
        return pagination
