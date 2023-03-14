from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name='main'),
    path('members/', views.members, name='members'),
    path('allMembers/', views.allMembers, name='allMembers'),
    path('allMembers/details/<slug:slug>', views.details, name='details'),
    path('testing/', views.testing, name='testing'), 
]
