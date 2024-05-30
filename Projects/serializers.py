from rest_framework import serializers
from .models import Project, Division, BoreHole, Sample

# create your serializers here
class SampleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sample
        fields = ['sample_number', 'depth_from', 'depth_to', 'sample_type', 'borehole', 'sample_description']

class BoreHoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = BoreHole
        fields = ['borehole', 'depth', 'receive_date']

class DivisionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Division
        fields = ['id', 'division']

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ['id', 'project', 'client', 'project_location_name', 'geometry_nodes', 'project_description']


