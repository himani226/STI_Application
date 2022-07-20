from django.urls import path
from django.contrib import admin
from . import views

#Djnago admin header custominzation

admin.site.site_header = "STI Admin Panel"
admin.site.site_title = "STI Admin Dashboard"
admin.site.index_title = "Welcome to STI Admin Panel"

urlpatterns = [
    path('', views.index, name='index'),
    path(r'index/', views.index, name='index'),
    path(r'about/', views.about, name='about'),
    path(r'challenges/', views.challenges, name='challenges'),
    path(r'contact/', views.contact, name='contact'),
    path(r'incubators/', views.incubators, name='incubators'),
    path(r'indicators/', views.indicators, name='indicators'),
    path(r'indicatorslist/', views.indicatorslist, name='indicatorslist'),
    path(r'indicatorsdef/', views.indicatorsdef, name='indicatorsdef'),
    path(r'pillarlist/', views.pillarlist, name='pillarlist'),
    path(r'instrumentation/', views.instrumentation, name='instrumentation'),
    path(r'portfolio/', views.portfolio, name='portfolio'),
    path(r'researchers/', views.researchers, name='researchers'),
    path(r'technology/', views.technology, name='technology'),

]
