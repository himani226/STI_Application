from django.http import HttpResponse
from django.shortcuts import render

from sti_app.models import HeaderMenu, FooterMenu, AboutData


def index(request):
    header_menu_name = HeaderMenu.objects.all()
    footer_menu_name = FooterMenu.objects.all()

    return render(request, 'base.html',
                  context={'header_menu_name': header_menu_name, 'footer_menu_name': footer_menu_name})


def about(request):
    about_data = AboutData.objects.all()
    header_menu_name = HeaderMenu.objects.all()
    footer_menu_name = FooterMenu.objects.all()
    return render(request, 'about.html', context={'about_data': about_data, 'header_menu_name': header_menu_name, 'footer_menu_name': footer_menu_name})


def indicators(request):
    return render(request, 'indicators.html')


def incubators(request):
    return render(request, 'incubators.html')


def instrumentation(request):
    return render(request, 'instrumentation.html')


def researchers(request):
    return render(request, 'researchers.html')


def portfolio(request):
    return render(request, 'portfolio.html')


def technology(request):
    return render(request, 'technology.html')


def challenges(request):
    return render(request, 'challenges.html')


def contact(request):
    return render(request, 'contact.html')
