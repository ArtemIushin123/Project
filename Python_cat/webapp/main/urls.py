from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.main_page),
    # <<<<<<< HEAD
    # =======
    path('test', views.get_test),
    # >>>>>>> main
    path('forms', views.forms_page),
    path('index', views.main_page)
]
