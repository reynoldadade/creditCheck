from django.shortcuts import render
from django.http import HttpResponse;
from django.template import loader


def index(request):
    template =loader.get_template('')
    return HttpResponse("Hello this is the eligibility index")


def detail(request,client_id):
    return HttpResponse("<h2>Details for client : " + client_id + "</h2>")