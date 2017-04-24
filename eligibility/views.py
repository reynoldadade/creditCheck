from django.shortcuts import render
from django.conf.urls import url
from django.http import Http404
from .models import Clients
from .forms import IdForm


def index(request):

    return render(request,'eligibility/details.html')


def detail(request,client_id):

    client = Clients.objects.get(employee_id=client_id)
    context = {'client_details':client}
    return render(request,'eligibility/details.html',context)
