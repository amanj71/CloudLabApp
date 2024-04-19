from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse, HttpResponse
import json
from .models import WaterContent, AjaxTest
from .forms import SamplesForm, WaterContentForm
from Projects.models import Project, Division, BoreHole, Sample

## Create your functional views here.
def select_related_objectsZZZZZ(request):
    projects = Project.objects.all()
    divisions = Division.objects.all()
    boreholes = BoreHole.objects.all()

    context = {
        'projects': projects,
        'divisions': divisions,
        'boreholes': boreholes,
    }
    return render(request, 'watercontent/watercontent.html', context)

def water_content_calculate(request):
    pass

def select_related_objects(request):
    if request.method == 'POST':
        form = SamplesForm(request.POST)
        if form.is_valid():
            print("HEre is view part ***************************")
            borehole = form.cleaned_data['borehole']
            samples = Sample.objects.filter(borehole_id=borehole.id)
            print(samples)
            
            return HttpResponse("data recieved")
    else:
        form = SamplesForm()
        return render(request, 'watercontent/watercontent.html', {'form': form})
    











#these two functions are for implemented dropdown buttons
def pass_divisions(request):
    data = json.loads(request.body)
    project_id = data['id']
    divisions = Division.objects.filter(project_id=project_id)
    return JsonResponse(list(divisions.values("id", "division")), safe=False)

def pass_boreholes(request):
    data = json.loads(request.body)
    division_id = data['id']
    boreholes = BoreHole.objects.filter(division_id=division_id)
    return JsonResponse(list(boreholes.values("id", "borehole")), safe=False)

#these two functions are for django-ajax training 
def test_ajax(request):
    content = AjaxTest.objects.all()
    return JsonResponse({'ajax': list(content.values())})

def form_test_ajax(request):
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        text = request.POST['text']
        
        new_ajax_test = AjaxTest(name=name, email=email, text=text)
        new_ajax_test.save()

    return HttpResponse("Created Successfully")

    
    
    
    
    
    
    
    
    
    
    
    