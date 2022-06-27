from django.http import HttpResponse
from django.shortcuts import render

from sti_app.models import Menu


def index(request):
    menu_name = Menu.objects.all()
    return render(request, 'index.html', context={'menu_name': menu_name})
