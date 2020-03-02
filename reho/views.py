from django.shortcuts import render

from services.models import Service


def index(request):
    menu_items = Service.objects.all()
    context = {
        'menu_items': menu_items
    }
    return render(request, 'index.html', context)