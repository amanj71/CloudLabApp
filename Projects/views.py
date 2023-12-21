from django.http import Http404, HttpResponse
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Project, Division, BoreHole, Sample
from .serializers import SampleSerializer, BoreHoleSerializer, DivisionSerializer, ProjectSerializer
from .forms import sample_formset

## Create your views here.

def index(request):
    projects = Project.objects.all()
    return render(request, "projects\projects.html", {"projects": projects})
    #strprojects = ", ".join([p.project for p in projects])
    #return HttpResponse(strprojects)

def projectdetail(request, proj_id):
    project = get_object_or_404(Project, id=proj_id)
    context = {'project': project}
    return render(request, 'projects\projectdetail.html', context)
    
def projectdetail_should_create_later():
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

## create your view_api here

@api_view(['GET', 'POST'])
def project_api(request):
    queryset = Project.objects.all()
    if request.method == 'GET':
        serializer = ProjectSerializer(queryset, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = ProjectSerializer(data=request.data)
        if serializer.is_valid:
            serializer.save()
            return Response('Project Added')
        else:
            return Response()
    
    
    
    
    #queryset = Project.objects.all()
    #serializer = ProjectSerializer(queryset, many=True)
    #return Response(serializer.data)

@api_view(['GET', 'PATCH', 'DELETE'])
def project_detail_api(request, proj_id):
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
