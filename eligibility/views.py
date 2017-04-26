from django.shortcuts import render
from django.conf.urls import url
from .models import Clients
from eligibility.forms import IdForm



def check_eligibility(request):
    if request.method =='POST': #if the form has been filled
        form = IdForm(request.POST)

        if form.is_valid(): # Data has gone through all the checks
            try:
                form=IdForm()
                employee_id = request.POST['employee_id']
                client = Clients.objects.get(employee_id=employee_id)
                context = {'client_details': client, 'message': True,'form':form}
            except Clients.DoesNotExist:
                return render(request,'eligibility/check_eligibility.html',{'message':'Client does not exist','form':form})
            return render(request, 'eligibility/check_eligibility.html', context)#redirect after post
    else:
        form = IdForm()#unbound form
        return render(request,'eligibility/check_eligibility.html',{'form':form,'message':'invalid transaction'})


def index(request):
    return render(request,'eligibility/check_eligibility.html')


# def detail(request,client_id):
#
#     client = Clients.objects.get(employee_id=client_id)
#     context = {'client_details':client}
#     return render(request,'eligibility/check_eligibility.html',context)
#
