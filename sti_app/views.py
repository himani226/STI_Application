import json

from django.http import HttpResponse, response
from django.shortcuts import render

from sti_app.responses.general_response import (no_success_response,
                                                   success_response)

from sti_app.models import HeaderMenu, FooterMenu, AboutData, HomeData, Spotlight, Stage, Pillar, Indicator


def index(request):
    header_menu_name = HeaderMenu.objects.all()
    footer_menu_name = FooterMenu.objects.all()
    home_data = HomeData.objects.all()
    spotlight = Spotlight.objects.all()

    return render(request, 'index.html',
                  context={'header_menu_name': header_menu_name, 'footer_menu_name': footer_menu_name,
                           'home_data': home_data, 'spotlight': spotlight})


def about(request):
    about_data = AboutData.objects.all()
    header_menu_name = HeaderMenu.objects.all()
    footer_menu_name = FooterMenu.objects.all()
    return render(request, 'about.html', context={'about_data': about_data, 'header_menu_name': header_menu_name,
                                                  'footer_menu_name': footer_menu_name})


def indicators(request):
    header_menu_name = HeaderMenu.objects.all()
    footer_menu_name = FooterMenu.objects.all()
    stage = Stage.objects.all()

    return render(request, 'indicators.html',
                  context={'header_menu_name': header_menu_name, 'footer_menu_name': footer_menu_name, 'stage': stage,
                           })


def indicatorslist(request):
    stage = request.POST.get('name')
    if stage:
        pillar_title = Pillar.objects.get(stage_title=stage)
        if pillar_title:
            response = success_response()
            response['message'] = 'Data deleted successfully'
        else:
            response = no_success_response()
    else:
        response = no_success_response()
    return HttpResponse(json.dumps(response))


def incubators(request):
    header_menu_name = HeaderMenu.objects.all()
    footer_menu_name = FooterMenu.objects.all()
    return render(request, 'incubators.html',
                  context={'header_menu_name': header_menu_name, 'footer_menu_name': footer_menu_name})


def instrumentation(request):
    header_menu_name = HeaderMenu.objects.all()
    footer_menu_name = FooterMenu.objects.all()
    return render(request, 'instrumentation.html',
                  context={'header_menu_name': header_menu_name, 'footer_menu_name': footer_menu_name})


def researchers(request):
    header_menu_name = HeaderMenu.objects.all()
    footer_menu_name = FooterMenu.objects.all()
    return render(request, 'researchers.html',
                  context={'header_menu_name': header_menu_name, 'footer_menu_name': footer_menu_name})


def portfolio(request):
    header_menu_name = HeaderMenu.objects.all()
    footer_menu_name = FooterMenu.objects.all()
    return render(request, 'portfolio.html',
                  context={'header_menu_name': header_menu_name, 'footer_menu_name': footer_menu_name})


def technology(request):
    header_menu_name = HeaderMenu.objects.all()
    footer_menu_name = FooterMenu.objects.all()
    return render(request, 'technology.html',
                  context={'header_menu_name': header_menu_name, 'footer_menu_name': footer_menu_name})


def challenges(request):
    header_menu_name = HeaderMenu.objects.all()
    footer_menu_name = FooterMenu.objects.all()
    return render(request, 'challenges.html',
                  context={'header_menu_name': header_menu_name, 'footer_menu_name': footer_menu_name})


def contact(request):
    header_menu_name = HeaderMenu.objects.all()
    footer_menu_name = FooterMenu.objects.all()
    return render(request, 'contact.html',
                  context={'header_menu_name': header_menu_name, 'footer_menu_name': footer_menu_name})
