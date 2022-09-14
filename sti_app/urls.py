from django.urls import path
from django.contrib import admin
from . import views

#Djnago admin header custominzation

admin.site.site_header = "STI Admin Panel"
admin.site.site_title = "STI Admin Dashboard"
admin.site.index_title = "Welcome to STI Admin Panel"

urlpatterns = [
    path('', views.index, name='Home'),
    path(r'Home/', views.index, name='Home'),
    path(r'About/', views.about, name='About'),
    path(r'Grand Challenges/', views.challenges, name='Grand Challenges'),
    path(r'contact/', views.contact, name='Contact'),
    path(r'Contact/', views.incubators, name='Incubators'),
    path(r'STI Indicators/', views.indicators, name='STI Indicators'),
    path(r'indicatorslist/', views.indicatorslist, name='indicatorslist'),
    path(r'indicatorsdef/', views.indicatorsdef, name='indicatorsdef'),
    path(r'pillarlist/', views.pillarlist, name='pillarlist'),
    path(r'Instrumentation Facilities/', views.instrumentation, name='Instrumentation Facilities'),
    path(r'IP Portfolio/', views.portfolio, name='IP Portfolio'),
    path(r'Researchers Network/', views.researchers, name='Researchers Network'),
    path(r'Technology Platform/', views.technology, name='Technology Platform'),
    path(r'techlist/', views.techlist, name='techlist'),
    path(r'Framework/', views.framework, name='Framework'),
    path(r'Help/', views.help, name='Help'),
    path(r'Website Policies/', views.policies, name='Website Policies'),
    path(r'Feedback/', views.feedback, name='Feedback'),
    path(r'Sitemap/', views.sitemap, name='Sitemap'),
    path(r'Accessibility/', views.accessibility, name='Accessibility'),

]
