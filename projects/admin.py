from django.contrib import admin

from projects.models import Project, Task


class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'order')

    list_filter = ('order',)


class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'created_at', 'order')
    list_filter = ('order',)


admin.site.register(Project, ProjectAdmin)
admin.site.register(Task, TaskAdmin)
