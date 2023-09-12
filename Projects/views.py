from django.http import Http404, HttpResponse
from django.shortcuts import render
from .models import ProjectList

# Create your views here.
def index(request):
    projects = ProjectList.objects.all()
    return render(request, "projects\projects.html", {"projects": projects})
    #return HttpResponse("Apps Started to be Creating")
