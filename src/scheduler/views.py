from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render

from .models import Floor


def index(request):
    try:
        floor_list = Floor.objects.order_by("name")
        template = loader.get_template("scheduler/index.html")
        context = {
            "floor_list": floor_list,
        }
    except Floor.DoesNotExist:
        raise Http404("The site encountered an error.")
    return render(request, "scheduler/index.html", context)


def floor(request, short_name):
    try:
        floor = Floor.objects.get(short_name=short_name)
    except Floor.DoesNotExist:
        raise Http404("Floor does not exist")
    return render(request, "scheduler/floor.html", {'floor': floor})


def period(request):
    return HttpResponse("Period")
