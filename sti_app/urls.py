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
    path(r'Grand_Challenges/', views.challenges, name='Grand_Challenges'),
    path(r'Contact/', views.contact, name='Contact'),
    path(r'Incubators/', views.incubators, name='Incubators'),
    path(r'STI_Indicators/', views.indicators, name='STI_Indicators'),
    path(r'indicatorslist/', views.indicatorslist, name='indicatorslist'),
    path(r'indicatorsdef/', views.indicatorsdef, name='indicatorsdef'),
    path(r'pillarlist/', views.pillarlist, name='pillarlist'),
    path(r'Instrumentation_Facilities/', views.instrumentation, name='Instrumentation_Facilities'),
    path(r'IP_Portfolio/', views.portfolio, name='IP_Portfolio'),
    path(r'Researchers_Network/', views.researchers, name='Researchers_Network'),
    path(r'Technology_Platform/', views.technology, name='Technology_Platform'),
    path(r'techlist/', views.techlist, name='techlist'),
    path(r'Framework/', views.framework, name='Framework'),
    path(r'Help/', views.help, name='Help'),
    path(r'Website_Policies/', views.policies, name='Website_Policies'),
    path(r'Feedback/', views.feedback, name='Feedback'),
    path(r'Sitemap/', views.sitemap, name='Sitemap'),
    path(r'Accessibility/', views.accessibility, name='Accessibility'),

]
