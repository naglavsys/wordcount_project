
from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage),
    path('about/', views.about, name = 'about'),
    path('count/', views.count, name = 'count'),
]
