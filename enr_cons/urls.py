from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('', views.enreg, name='enreg'),
    path('consultation/', views.consult, name='consult'),
]
