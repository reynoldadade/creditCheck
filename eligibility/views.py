from django.shortcuts import render
from django.conf.urls import url
from django.http import Http404
from .models import Clients


def index(request):

    return render(request,'eligibility/index.html')


def detail(request,client_id):
   try:
       client = Clients.objects.get(employee_id=client_id)

       context = {'client_details':client}
       return render(request,'eligibility/details.html',context)
   except Clients.DoesNotExist:
       raise Http404("Album Does Not Exist")
