from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from .forms import ContactForm

# Create your views here.

def home_page(request):
    
    context = {

    }
    return render(request, 'home/home.html', context)

def login_page(request):
    return redirect('admin:index')

def contact_page(request):
    contact_form = ContactForm(request.POST or None)
    context = {
        "contact_form": contact_form,
    }
    return render(request, 'home/contact.html', context)

def about_page(request):
    
    context = {

    }
    return render(request, 'home/about.html', context)


