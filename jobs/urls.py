from django.conf.urls import url

from .views import TaskListView, TaskDetailView, TaskEditView, TaskLogListView

urlpatterns = [
    url(r'^task/list/$', TaskListView.as_view(), name="task_list"),
    url(r'^task/info/(?P<pk>[0-9]+)/$', TaskDetailView.as_view(), name="task_detail"),
    url(r'^task/edit/(?P<pk>[0-9]+)/$', TaskEditView.as_view(), name="task_edit"),
    url(r'^task/log/(?P<pk>[0-9]+)/$', TaskLogListView.as_view(), name="task_log"),
]
