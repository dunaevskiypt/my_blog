from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.template import context


def index(request):
    context = {"title": "Home"}

    return render(request, "main/index.html", context=context)


def about(request):
    return HttpResponse("About page")
