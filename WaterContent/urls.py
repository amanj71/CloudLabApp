from django.urls import path
from . import views

app_name = "WaterContent"

urlpatterns = [
    path('', views.select_related_objects, name="test_wc"),
    path('divi/', views.pass_divisions, name="pass_divisions"),
    #path('', views.select_related_objects, name="test_wc"),
    path('testajax/', views.test_ajax, name='test_ajax'),
    path('formajax/', views.form_test_ajax, name='form_test_ajax'),
    path('1221', views.water_content_calculate, name="water_content_calculate"),
]
