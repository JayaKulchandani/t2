from django.contrib import admin
from django.urls import path
from . import views 

urlpatterns = [
    path('hello/',views.hello),
    path('index/', views.index),
    path('member/',views.members),
    path('template/',views.testing),
    path('studentindex/', views.studentindex),
]
