from django.shortcuts import render, redirect
from django.http import HttpRequest,HttpResponse
from .models import Hospital, Tiffin_service_provider
from .forms import ServiceProviderForm
import requests
import json
from plotly.graph_objs import Bar, Layout
from plotly import offline
import csv
import os
import datetime




def home(request):  
    if request.method == 'GET':
        form = ServiceProviderForm()   
        date_today = datetime.date.today()
        hospitals = Hospital.objects.all()
        context = {
            'hospitals':hospitals,
            'date':date_today,
            'form':form
        }
        return render(request, 'Home.html',context)
    

def Find_food(request):
    if request.method=='POST':
        location_name = request.POST['find_food']
        print(location_name)
        try:
            tiffin_providers = Tiffin_service_provider.objects.filter(location__iexact=location_name)

        except:
            return HttpResponse('No registerd service provider found, If you know somebody, ask them to register')
        
        context = {
            'tiffins':tiffin_providers,
            
        }
        return render(request, 'tiffin.html',context)
    else:
        return redirect('/')

def Find_O2(request):
    if request.method=='POST':
        find_o2 = request.POST['find_O2']
        try:
            oxygen_provider = Tiffin_service_provider.objects.filter(location__iexact=find_o2)

        except:
            return HttpResponse('No registerd service provider found, If you know somebody, ask them to register')
        
        context = {
            'oxygens':oxygen_provider,
            
        }
        return render(request, 'oxygen.html',context)
    else:
        return redirect('/')



def Register(request):
    if request.method == 'POST':
        form = ServiceProviderForm(request.POST)
        print(dform['mobile']['value'])
        
        if form.is_valid():
            form.save()
            return HttpResponse('response saved successfully')
        else:
            return HttpResponse('failed request')
    if request.method == "GET":
        return redirect('/')

