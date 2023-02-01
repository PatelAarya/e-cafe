from django.urls import path
from . import views

urlpatterns = [
    
    path('index/', views.index, name='index'),
    path('registration/', views.registration, name='registration'),
    path('about/', views.about, name='about'),
    path('gallery/', views.gallery, name='gallery'),
    path('menu/', views.menu, name='menu'),
    path('reservation/', views.reservation, name='reservation'),
    path('contact/', views.contact, name='contact'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('feedback/', views.feedback, name='feedback'),
    path('cart/', views.cartLogic, name='cart'),
    path('foodSerializerApi/', views.foodSerializerApi, name='foodSerializerApi'),
    path('categorySerializerApi/', views.categorySerializerApi, name='categorySerializerApi'),
    
    path('food_submit/', views.food_submit, name='food_submit'),
    
    
    
    
    
    
    
    
    
    
    
]

