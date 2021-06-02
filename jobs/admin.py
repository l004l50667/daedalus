from django.contrib import admin

from .models import Category, Task

# Register your models here.


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'display', 'create_user')


class TaskAdmin(admin.ModelAdmin):
    list_display = ('name', 'type', 'category', 'path')

admin.site.register(Category, CategoryAdmin)
admin.site.register(Task, TaskAdmin)
