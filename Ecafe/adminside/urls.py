from django.urls import path
from . import views

urlpatterns = [
    path('demo/', views.demo), 
    path('adminside_index/', views.adminside_index, name='adminside_index'),
    path('adminside_charts/', views.adminside_charts, name='adminside_charts'),
    path('adminside_forms/', views.adminside_forms, name='adminside_forms'),
    
    path('adminside_login/', views.adminside_login, name='adminside_login'),
    path('adminside_register/', views.adminside_register, name='adminside_register'),
    path('adminside_tables/', views.adminside_tables, name='adminside_tables'),
    
    
    
    

    
       
    
]

