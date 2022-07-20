import json

from django.http import HttpResponse, response
from django.shortcuts import render

from sti_app.responses.general_response import (no_success_response,
                                                   success_response)

from sti_app.models import HeaderMenu, FooterMenu, AboutData, HomeData, Spotlight, Stage, Pillar, Indicator, \
    IndicatorDefinition, HomeFramework, HomePlanPolicies


def index(request):
    header_menu_name = HeaderMenu.objects.all()
    footer_menu_name = FooterMenu.objects.all()
    home_data = HomeData.objects.all()
    spotlight = Spotlight.objects.all()
    framework = HomeFramework.objects.all()
    policies = HomePlanPolicies.objects.all()
    return render(request, 'index.html',
                  context={'header_menu_name': header_menu_name, 'footer_menu_name': footer_menu_name,
                           'home_data': home_data, 'spotlight': spotlight, 'framework':framework, 'policies':policies})


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


def pillarlist(request):
    stage = request.GET.get('name')
    if stage:
        pillar_title = Pillar.objects.filter(stage_title=stage)
        if pillar_title:
            all_pillar = []
            response = success_response()
            for pillar in pillar_title:
                all_pillar.append(pillar.embed())
            response['pillar'] = all_pillar

            return HttpResponse(json.dumps(response))
        else:
            response = no_success_response()
    else:
        response = no_success_response()
    return HttpResponse(json.dumps(response))


def indicatorslist(request):
    pillar = request.GET.get('id')
    if pillar:
        indi_title = Indicator.objects.filter(pillar_title_id=pillar)
        if indi_title:
            all_ind = []
            response = success_response()
            for ind in indi_title:
                all_ind.append(ind.embed())
            response['indicators'] = all_ind

            return HttpResponse(json.dumps(response))
        else:
            response = no_success_response()
    else:
        response = no_success_response()
    return HttpResponse(json.dumps(response))


def indicatorsdef(request):
    indi_id = request.GET.get('id')
    if indi_id:
        indi_title = IndicatorDefinition.objects.filter(indicator_title_id=indi_id)
        if indi_title:
            all_indef = []
            response = success_response()
            for indef in indi_title:
                all_indef.append(indef.embed())
            response['indi_def'] = all_indef
            return HttpResponse(json.dumps(response))
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
