from django.http import Http404, HttpResponse
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.core.exceptions import ObjectDoesNotExist
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.viewsets import ModelViewSet
from .models import Project, Division, BoreHole, Sample
from .serializers import SampleSerializer, BoreHoleSerializer, DivisionSerializer, ProjectSerializer
from .forms import sample_formset


## Create your views here.

def projects(request):
    projects = Project.objects.all()
    return render(request, "projects/projects.html", {"projects": projects})
    #strprojects = ", ".join([p.project for p in projects])
    #return HttpResponse(strprojects)

def projectdetail(request, slug):
    project = get_object_or_404(Project, slug=slug)
    division = Division.objects.filter(project_id=project.id)
    if division:
        divi = division
        print(type(divi))
    else:
        divi = Division.objects.none()
        print("****IS NOT ITERATIVE****")
        print(type(divi))
        print(divi)
    context = {'project': project, 'division': divi}
    return render(request, 'projects/project_detail.html', context)

def divisiondetail(request, slug):
    division = get_object_or_404(Division, slug=slug)
    project = get_object_or_404(Project, id=division.project_id,) 
    boreholes = BoreHole.objects.filter(division_id=division.id)
    boreholes_count = boreholes.count()

    
    context = {'boreholes': boreholes, 'boreholes_count': boreholes_count, 'division': division,
                'project': project}
    
    return render(request, 'projects/division_detail.html', context)

def boreholedetail(request, slug):
    borehole = get_object_or_404(BoreHole, slug=slug)
    samples = Sample.objects.filter(borehole_id=borehole.id)
    context = {
        'borehole': borehole, 'samples': samples,
    }
    return render(request, 'projects/borehole_detail.html', context)

def form_projectdetail_should_create_later():
    sam_formset = sample_formset(queryset=Sample.objects.all())
    if request.method == 'POST':
        sam_formset = sample_formset(request.POST)
        if sam_formset.is_valid():
            sam_formset.save()
            return HttpResponseRedirect('Added Correctly :)') 
    else:
        sam_formset = sam_formset
    
    projdetail = get_object_or_404(Project, id=proj_id)
    division = Division.objects.filter(project_id=proj_id)
    
    context = {"projdetail": projdetail, 'division': division,'sam_formset': sam_formset}
    return render(request, "projects\projectdetail.html", context)

## Create Your API Views Here
# functional views api
@api_view(['GET', 'POST'])
def project_api(request):
    queryset = Project.objects.all()
    if request.method == 'GET':
        serializer = ProjectSerializer(queryset, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = ProjectSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response('Project Added')
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    
    
    
    #queryset = Project.objects.all()
    #serializer = ProjectSerializer(queryset, many=True)
    #return Response(serializer.data)

@api_view(['GET', 'PATCH', 'DELETE'])
def projectdetail_api(request, proj_id):
    project = get_object_or_404(Project, id=proj_id)
    if request.method == 'GET':
        serializer = ProjectSerializer(project)
        return Response(serializer.data)
    elif request.method == "POST":
        serializer = ProjectSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response('POST is Saved')
    elif request.method == "PATCH":
        serializer = ProjectSerializer(project, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response('POST is Updated')
    elif request.method == "DELETE":
        project.delete()
        return Response("The Poj has been deleted")

@api_view(['GET'])
def divisiondetail_api(request):
    division = get_object_or_404(Division, id=div_id, project_id=proj_id)
    serializer = DivisionSerializer(division)
    return Response(serializer.data)


# class based views api
class ProjectViewSetAPI(ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

class DivisionViewSetAPI(ModelViewSet):
    queryset = Division.objects.all()
    serializer_class = DivisionSerializer

class BoreHoleViewSetAPI(ModelViewSet):
    queryset = BoreHole.objects.all()
    serializer_class = BoreHoleSerializer

class SampleViewSetAPI(ModelViewSet):
    queryset = Sample.objects.all()
    serializer_class = SampleSerializer