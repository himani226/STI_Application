from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('sti_indicators/', views.indicators, name='indicators'),
    path('about/', views.index, name='about'),
    path('about/', views.index, name='about'),
    path('about/', views.index, name='about'),
]
