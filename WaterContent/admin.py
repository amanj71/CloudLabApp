from django.contrib import admin
from .models import WaterContent, AjaxTest
from Projects.models import Project, Division, BoreHole, Sample

# Register your models here.
@admin.register(WaterContent)
class WaterContentAdmin(admin.ModelAdmin):
    list_display=('project', 'borehole', 'sample', 'get_sample_depth',)
    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == 'division':
            # Get the selected project from the form data
            selected_project = request.POST.get('project')
            print("******************************** select_project")
            print(selected_project)
            if selected_project:
                try:
                    #selected_project_id = int(selected_project)
                    kwargs['queryset'] = Division.objects.filter(project_id=selected_project)
                except ValueError:
                    pass  # Handle invalid project ID (e.g., non-integer input)
        return super().formfield_for_foreignkey(db_field, request, **kwargs)



## Register models directly
admin.site.register(AjaxTest)
    