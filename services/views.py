from django.shortcuts import render, get_object_or_404, redirect

from .models import Service
from .forms import ServiceModelForm

def services_list(request):
    all_services = Service.objects.all()
    
    context = {
        'all_services': all_services
    }
    return render(request, 'services/services_list.html', context)


def service_detail(request, slug):
    service = get_object_or_404(Service, slug=slug)

    context = {
        'service': service
    }
    return render(request, 'services/service_detail.html', context)


def service_create(request):
    form = ServiceModelForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('/sevices/')

    context = {
        'form': form
    }
    return render(request, 'services/service_create.html', context)