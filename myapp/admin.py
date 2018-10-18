from django.contrib import admin
from .models import Editor,Project,tags,Comment

class ProjectAdmin(admin.ModelAdmin):
    filter_horizontal =('tags',)


admin.site.register(Editor)
admin.site.register(Project, ProjectAdmin)
admin.site.register(tags)
admin.site.register(Comment)