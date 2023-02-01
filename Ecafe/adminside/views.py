from multiprocessing import context
from django.shortcuts import render
from django.http.response import HttpResponse
import requests


# Create your views here.


def demo(request):
    return HttpResponse("Hello World")


def adminside_index(request):
    return render(request,'adminside_index.html')

def adminside_charts(request):
    return render(request,'adminside_charts.html')

def adminside_forms(request):
    category_data = requests.get("http://127.0.0.1:8000/Brothers_cafe/categorySerializerApi/")
    category_object = category_data.json()
    context3 = {"category_object": category_object}   
    
    return render(request,'adminside_forms.html', context3)
    

def adminside_login(request):
    return render(request,'adminside_login.html')

def adminside_register(request):
    return render(request,'adminside_register.html')

def adminside_tables(request):
    
    tabletype = request.GET.get('typetable')
    print(tabletype)
    print(type(tabletype))
    if tabletype == 'foodtable':
        print("Yes i can do it ")
        food_data = requests.get("http://127.0.0.1:8000/Brothers_cafe/foodSerializerApi/")
        food_object = food_data.json()
        context = {"food_object": food_object}   
        
   
        return render(request,'adminside_tables.html', context)
    
    else:
        category_data = requests.get("http://127.0.0.1:8000/Brothers_cafe/categorySerializerApi/")
        category_object = category_data.json()
        context2 = {"category_object": category_object}   
    
        return render(request,'adminside_tables.html', context2)

