import json

from django.http import HttpResponse, response
from django.shortcuts import render

from sti_app.responses.general_response import (no_success_response,
                                                success_response)

from sti_app.models import HeaderMenu, FooterMenu, AboutData, HomeData, Spotlight, Stage, Pillar, Indicator, \
    IndicatorDefinition, HomePlanPolicies, HomeSlider, Banner, TechnologyArea, TechnologyAreaDetail, Contributor


def index(request):
    header_menu_name = HeaderMenu.objects.all()
    footer_menu_name = FooterMenu.objects.all()
    slider = HomeSlider.objects.all()
    home_data = HomeData.objects.all()
    spotlight = Spotlight.objects.all()
    framework = Stage.objects.all()
    policies = HomePlanPolicies.objects.all()
    banner = Banner.objects.all()
    return render(request, 'index.html',
                  context={'header_menu_name': header_menu_name, 'footer_menu_name': footer_menu_name, 'slider': slider,
                           'home_data': home_data, 'spotlight': spotlight, 'framework': framework,
                           'policies': policies, 'banner': banner})


def about(request):
    about_data = AboutData.objects.all()
    header_menu_name = HeaderMenu.objects.all()
    footer_menu_name = FooterMenu.objects.all()
    banner = Banner.objects.all()
    contributor = Contributor.objects.all()
    return render(request, 'about.html', context={'about_data': about_data, 'header_menu_name': header_menu_name,
                                                  'footer_menu_name': footer_menu_name, 'banner': banner,'contributor':contributor})


def indicators(request):
    header_menu_name = HeaderMenu.objects.all()
    footer_menu_name = FooterMenu.objects.all()
    stage = Stage.objects.all()
    banner = Banner.objects.all()
    return render(request, 'indicators.html',
                  context={'header_menu_name': header_menu_name, 'footer_menu_name': footer_menu_name, 'stage': stage,
                           'banner': banner})


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


def technology(request):
    header_menu_name = HeaderMenu.objects.all()
    footer_menu_name = FooterMenu.objects.all()
    banner = Banner.objects.all()
    tech_area = TechnologyArea.objects.all()
    return render(request, 'technology.html',
                  context={'header_menu_name': header_menu_name, 'footer_menu_name': footer_menu_name,
                           'tech_area': tech_area,
                           'banner': banner})


def techlist(request):
    tech_area = request.GET.get('name')
    if tech_area:
        tech_name = TechnologyAreaDetail.objects.filter(technology_area_name_id=tech_area)
        if tech_name:
            all_tech_name = []
            response = success_response()
            for tech_area_name  in tech_name:
                all_tech_name.append(tech_area_name.embed())
            response['all_tech_name'] = all_tech_name
            return HttpResponse(json.dumps(response))
        else:
            response = no_success_response()
    else:
        response = no_success_response()
    return HttpResponse(json.dumps(response))


def incubators(request):
    header_menu_name = HeaderMenu.objects.all()
    footer_menu_name = FooterMenu.objects.all()
    banner = Banner.objects.all()
    return render(request, 'incubators.html',
                  context={'header_menu_name': header_menu_name, 'footer_menu_name': footer_menu_name,
                           'banner': banner})


def framework(request):
    header_menu_name = HeaderMenu.objects.all()
    footer_menu_name = FooterMenu.objects.all()
    banner = Banner.objects.all()
    return render(request, 'framework.html',
                  context={'header_menu_name': header_menu_name, 'footer_menu_name': footer_menu_name,
                           'banner': banner})


def instrumentation(request):
    header_menu_name = HeaderMenu.objects.all()
    footer_menu_name = FooterMenu.objects.all()
    banner = Banner.objects.all()
    return render(request, 'instrumentation.html',
                  context={'header_menu_name': header_menu_name, 'footer_menu_name': footer_menu_name,
                           'banner': banner})


def researchers(request):
    header_menu_name = HeaderMenu.objects.all()
    footer_menu_name = FooterMenu.objects.all()
    banner = Banner.objects.all()
    return render(request, 'researchers.html',
                  context={'header_menu_name': header_menu_name, 'footer_menu_name': footer_menu_name,
                           'banner': banner})


def portfolio(request):
    header_menu_name = HeaderMenu.objects.all()
    footer_menu_name = FooterMenu.objects.all()
    banner = Banner.objects.all()
    return render(request, 'portfolio.html',
                  context={'header_menu_name': header_menu_name, 'footer_menu_name': footer_menu_name,
                           'banner': banner})


def challenges(request):
    header_menu_name = HeaderMenu.objects.all()
    footer_menu_name = FooterMenu.objects.all()
    banner = Banner.objects.all()
    return render(request, 'challenges.html',
                  context={'header_menu_name': header_menu_name, 'footer_menu_name': footer_menu_name,
                           'banner': banner})


def contact(request):
    header_menu_name = HeaderMenu.objects.all()
    footer_menu_name = FooterMenu.objects.all()
    banner = Banner.objects.all()
    return render(request, 'contact.html',
                  context={'header_menu_name': header_menu_name, 'footer_menu_name': footer_menu_name,
                           'banner': banner})


def help(request):
    header_menu_name = HeaderMenu.objects.all()
    footer_menu_name = FooterMenu.objects.all()
    banner = Banner.objects.all()
    return render(request, 'help.html',
                  context={'header_menu_name': header_menu_name, 'footer_menu_name': footer_menu_name,
                           'banner': banner})


def feedback(request):
    header_menu_name = HeaderMenu.objects.all()
    footer_menu_name = FooterMenu.objects.all()
    banner = Banner.objects.all()
    return render(request, 'feedback.html',
                  context={'header_menu_name': header_menu_name, 'footer_menu_name': footer_menu_name,
                           'banner': banner})


def sitemap(request):
    header_menu_name = HeaderMenu.objects.all()
    footer_menu_name = FooterMenu.objects.all()
    banner = Banner.objects.all()
    return render(request, 'sitemap.html',
                  context={'header_menu_name': header_menu_name, 'footer_menu_name': footer_menu_name,
                           'banner': banner})


def policies(request):
    header_menu_name = HeaderMenu.objects.all()
    footer_menu_name = FooterMenu.objects.all()
    banner = Banner.objects.all()
    return render(request, 'policies.html',
                  context={'header_menu_name': header_menu_name, 'footer_menu_name': footer_menu_name,
                           'banner': banner})


def accessibility(request):
    header_menu_name = HeaderMenu.objects.all()
    footer_menu_name = FooterMenu.objects.all()
    banner = Banner.objects.all()
    return render(request, 'accessibility.html',
                  context={'header_menu_name': header_menu_name, 'footer_menu_name': footer_menu_name,
                           'banner': banner})
