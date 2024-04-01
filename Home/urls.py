from django.urls import path
from django.views.generic import TemplateView
from . import views

app_name = 'Home'

urlpatterns = [
    path('', views.home_page, name="home_page"),
    path('login/', views.login_page, name="login_page"),
    path('contact/', views.contact_page, name="contact_page"),
    path('about/', views.about_page, name="about_page"),
    path('template/', TemplateView.as_view(template_name='template.html'), name="template"),
    path('templaty/', TemplateView.as_view(template_name='template_check.html'), name="templaty"),
]