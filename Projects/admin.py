from django.contrib import admin
from . import models

# define classes here
class ProjectAdmin(admin.ModelAdmin):
    exclude = ('user_company',)
    list_display = ("project", "client", "project_location_name")

@admin.register(models.Division)
class DivisionAdmin(admin.ModelAdmin):
    list_display = ('division', "project")

# Register your models here.
admin.site.register(models.Project, ProjectAdmin)
