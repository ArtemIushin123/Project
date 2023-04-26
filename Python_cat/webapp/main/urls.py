from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.main_page),
    path('index', views.main_page, name='index'),
    path('forms', views.forms_page),
    path('service', views.service_page),
    path('timetable', views.timetable_page)

]
