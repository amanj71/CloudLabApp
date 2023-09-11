from django.contrib import admin
from . import models

# define classes here
class ProjectListAdmin(admin.ModelAdmin):
    exclude = ('user_company',)
    list_display = ("project", "client", "project_location_name")

# Register your models here.
admin.site.register(models.ProjectList, ProjectListAdmin)
