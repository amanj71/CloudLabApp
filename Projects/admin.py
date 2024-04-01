from django.contrib import admin
from . import models

# define classes here
class ProjectAdmin(admin.ModelAdmin):
    exclude = ('user_company',)
    list_display = ("project", "client", "project_location_name")

@admin.register(models.Division)
class DivisionAdmin(admin.ModelAdmin):
    list_display = ('division', "project")

@admin.register(models.BoreHole)
class BoreHoleAdmin(admin.ModelAdmin):
    list_display = ('borehole', 'depth',)

@admin.register(models.Sample)
class SampleAdmin(admin.ModelAdmin):
    list_display = ('borehole','sample_number', 'depth_from', 'sample_type', 'sample_description')

# Register your models here.
admin.site.register(models.Project, ProjectAdmin)
