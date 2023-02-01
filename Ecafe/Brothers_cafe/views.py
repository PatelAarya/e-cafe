from importlib.resources import Resource
from itertools import count, product
from urllib import response
from django.shortcuts import render, redirect, HttpResponseRedirect
from django.http.response import HttpResponse
from .models import *
from django.contrib import messages
from django.contrib.auth import logout
from django.contrib.auth import authenticate
from django.http import JsonResponse
from . serializers import categorySerializer, foodSerializer
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status
from rest_framework.response import Response
from django.contrib.auth.decorators import login_required

# Create your views here.

@csrf_exempt
def foodSerializerApi(request):
    if request.method =="POST":
            
            # food_id = request.POST['food_id']
            # food_name = request.POST.get('food_name')
            # print(food_id, food_name)
            # # obj1 = food(fname=fname, lname=lname,email=email, message=message)
            # # obj1.save()
            
            serializer = foodSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)

    if request.method == "GET":
        foods = food.objects.all()
        food_Serializer = foodSerializer(foods, many=True)
        return JsonResponse(food_Serializer.data, safe=False)
    
@csrf_exempt   
def categorySerializerApi(request):

    
        category_tables = category_table.objects.all()
        category_Serializer = categorySerializer(category_tables, many=True)
        return JsonResponse(category_Serializer.data, safe=False)
    

@csrf_exempt
def cartLogic(request):
    if request.method =="POST":
        food_item = request.POST['food_item']
        food_item = food_item.replace("[","").replace("]","").replace('"',"")
        food_item = food_item.split(",")

        aaa = food.objects.values("food_name", "id")
        print("0000000000000000000000000000111111111111>>", aaa)
        
        food_id = []
        for i in food_item:
            fid = food.objects.filter(food_name=i).values_list('id', flat=True)
            food_id.append(fid)
            print(fid, "@@@@@@@@@@@@@@@@@@@2222")
            
            
        food_price = request.POST['food_price']
        food_price = food_price.replace("[","").replace("]","").replace('"',"")
        food_price = food_price.split(",")

        food_quantity = request.POST['food_quantity']
        food_quantity = food_quantity.replace("[","").replace("]","").replace('"',"")
        food_quantity = food_quantity.split(",")
 
        customer_name = request.POST.get('customer_name')

        
        user_name = user_registration.objects.filter(fname=customer_name)
        user_id = user_name.values_list('id', flat=True)
        
        print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>",food_item, food_price, food_quantity, user_id)
        for j in range(len(food_item)):
            print(j)
            total_price = food_quantity[j] * food_price[j]
            obj1 = cart(food_name_id=food_id[j], customer_name_id=user_id,food_quantity=int(food_quantity[j]),food_price=int(food_price[j]) ,total = total_price)
            obj1.save()
        
    return render(request, 'cart.html')







def index(request):
    gal_cat = GalleryCategory.objects.all()
    
    return render(request,'index.html',{'gal_cat':gal_cat})

def about(request):
    gal_cat = GalleryCategory.objects.all()

    return render(request,'about.html',{'gal_cat':gal_cat})




def gallery(request):
    gal_cat = GalleryCategory.objects.all()
    galleryid = request.GET.get('gal')
    print(galleryid)
    
    if galleryid:
        obj99 = GalleryImage.objects.filter(categoryGalery = galleryid)
        return render(request, 'gallery.html', {'fgh123':obj99,'gal_cat':gal_cat})
    return render(request, 'gallery.html', {'gal_cat':gal_cat})
    
def menu(request):
    gal_cat = GalleryCategory.objects.all()

    obj2 = category_table.objects.all()
    
    categoryid = request.GET.get('cat')
    
    if categoryid:
        obj = food.objects.filter(categoty = categoryid)
    else:
        obj = food.objects.all()
    
    return render(request,'menu.html', {'form':obj, 'cat':obj2,'gal_cat':gal_cat})
@csrf_exempt
def food_submit(request):
    if request.method == 'POST':
        print(request.POST, "$$$$$$$$$$")
        food_name= request.POST['food_name']
        categoty= request.POST['categoty']
        description= request.POST['description']
        price= request.POST['price']
        image= request.POST['image']
        print(price)
        category_id = category_table.objects.filter(id= categoty)
        
        obj1 = food(food_name=food_name, categoty_id=category_id,description=description,price=float(price),image=image)
        obj1.save()
        return JsonResponse({'data successfully added'})

def reservation(request):
    gal_cat = GalleryCategory.objects.all()
    
    if request.method == 'POST':
        name = request.POST['name']
        people = request.POST['people']
        bookingDate = request.POST['bookingDate']
        obj1 = Reservation(name=name, people=people,created_at=bookingDate)
        obj1.save()
        print(name, people , bookingDate)
    return render(request,'reservation.html',{'gal_cat':gal_cat})

def contact(request):
    gal_cat = GalleryCategory.objects.all()
    
    if request.method == 'POST':
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        message = request.POST['message']
        
        obj1 = contact_form(fname=fname, lname=lname,email=email, message=message)
        obj1.save()
        
        return redirect('login',{'gal_cat':gal_cat})
    
    else:
        return render(request, 'contact.html',{'gal_cat':gal_cat})

@csrf_exempt
def login(request):
    gal_cat = GalleryCategory.objects.all()
    
    if request.method=='POST':
        print("283y42878248273ryiuhdf")
        email = None
        try:
            fname = request.POST['fname']
            email = request.POST['email']
            password = request.POST['password']
        except:
            fname = request.POST.get('fname')
            password = request.POST.get('password')        
        if email:
            obj3 = user_registration.objects.filter(fname=fname, email=email, password=password).count()
            obj4 = user_registration.objects.filter(fname=fname, email=email, password=password)
            if obj3>0:
                request.session['is_loged'] = fname
                request.session['unique'] = obj4[0].fname
                # user_details = UserLogInDetails.objects.filter(fname=fname, email=email, password=password)
                # user_login_count = user_details.count
                # logged_in = datatime.nnow()
                # count += 1
                # .save()
                
        obj1 = user_registration.objects.filter(fname=fname, password=password)
        if obj1:
            request.session['is_loged'] = fname
            return JsonResponse({"success":True, "user":fname})
            
            
        
    return render(request,'login.html',{'gal_cat':gal_cat})

   

def registration(request):
    gal_cat = GalleryCategory.objects.all()
    
    if request.method == 'POST':
        fname = request.POST['fname']
        lname = request.POST['lname']
        number = request.POST['number']
        email = request.POST['email']
        password = request.POST['password']
                
        register = user_registration.objects.all()
        for i in register:
            if i.email == email:
                messages.error(request,"Email already exist. Please Login")
                return render(request, 'registration.html')
            
        obj2 = user_registration(fname=fname, lname=lname, number=number, email=email, password=password)
        obj2.save()
        
        # return HttpResponse("Successful")
        return redirect('login')
    
    else:
        return render(request, 'registration.html',{'gal_cat':gal_cat})
        

def logout(request):
    if request.session.has_key('is_loged'):
        del request.session['is_loged']
        try:
            del request.session['unique']
            return redirect('index')
        except:
            
            return redirect('adminside_login')
     
    
    
    return redirect('contact')

# def logout(request):
#     logout(request)
#     return redirect('index')


def feedback(request):
    return render(request,'feedback.html')


# def updateItem(request):
    
    
#     data = json.loads(request.body)
#     print(data)
#     print("sasi")
#     productId = data['productId']
#     action = data['action']
#     print('Action',action)
#     print('productId', productId)
    
#     # customer = request.user.customer
#     # print('Customer:',customer)
#     return JsonResponse('Item was added', safe=False)