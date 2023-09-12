from django.http import Http404, HttpResponse
from django.shortcuts import render, get_object_or_404
from .models import ProjectList

# Create your views here.
def index(request):
    projects = ProjectList.objects.all()
    return render(request, "projects\projects.html", {"projects": projects})
    #strprojects = ", ".join([p.project for p in projects])
    #return HttpResponse(strprojects)

def projectdetail(request, project_id):
    projdetail = get_object_or_404(ProjectList, id=project_id)
    context = {"projdetail": projdetail}
    return render(request, "projects\projectdetail.html", context)

