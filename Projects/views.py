from django.http import Http404, HttpResponse
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from .models import Project, Division, BoreHole, Sample
from .forms import sample_formset

# Create your views here.
def index(request):
    projects = Project.objects.all()
    return render(request, "projects\projects.html", {"projects": projects})
    #strprojects = ", ".join([p.project for p in projects])
    #return HttpResponse(strprojects)

def projectdetail(request, proj_id):
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



#def add_divisions(request):
#    if request.method == 'POST':
#        sam_formset = sample_formset(request.POST)
#        if sam_formset.is_valid():
#            sam_formset.save()
#            return redirect('Added Correctly :)') 
#        else:
#            sam_formset = sample_formset()
#    context = {'sam_formset': sam_formset}
#    return render(request, 'projects\projectdetail.html', context)
