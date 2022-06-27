from django.http import HttpResponse
from .models import Menu


def index(request):
    Menu.object.all()
    