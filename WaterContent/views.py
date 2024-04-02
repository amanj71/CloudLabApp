from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse, HttpResponse
import json
from .models import WaterContent, AjaxTest
from .forms import WaterContentForm
from Projects.models import Project, Division, BoreHole, Sample

# Create your views here.
from django.shortcuts import render

def select_related_objects(request):
    form = WaterContentForm()
    if request.method == "POST":
        form = WaterContentForm(request.POST)
        if form.is_valid():
            print("Got Form Printed here (From Views.py)********")
            print(form)
    context = {
        "form": form
    }
    return render(request, 'watercontent/watercontent.html', context)



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


def water_content_calculate(request):
    pass
    
    
    
    
    
    
    
    
    
    
    
    