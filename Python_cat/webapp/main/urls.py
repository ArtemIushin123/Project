from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.main_page),
<<<<<<< HEAD
=======
    path('appointment', views.appointment),
    path('contacts1', views.contacts1),
    path('test', views.get_test)
>>>>>>> main
]
