import datetime
from email.policy import default
from enum import auto
from tkinter import CASCADE
from tkinter.tix import AUTO
from xml.dom.minidom import Attr
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django.utils import timezone

# Create your models here.
class UserLogInDetails(models.Model):
    # username = foreignKey
    # loggedin_count =  intkey
    # last_logged_in = datetime
    # last_logged_out = datetime
    # contact_count = integerfield
    # contact_message = int
    # reservation_count = int
    #reserved_by = char
    pass

class category_table(models.Model):
    # category_id = models.IntegerField(blank=True, null=True, unique=True)
    category_name = models.CharField(max_length=25 ,blank=True , null=True)
    
    def __str__(self):
        return self.category_name

class food(models.Model):
    # food_id = models.IntegerField(unique=True)
    categoty = models.ForeignKey(category_table, on_delete=models.CASCADE)
    food_name = models.CharField(max_length=25)
    description = models.TextField()
    price = models.IntegerField()
    image = models.ImageField(upload_to='Brothers_cafe/images', default="")
    like = models.IntegerField(null=True, blank=True, default=0)
    dislike = models.IntegerField(null=True, blank=True, default=0)
    
    def __str__(self):
        return (self.food_name)   
    

class user_registration(models.Model):
    fname = models.CharField(max_length=15)
    lname = models.CharField(max_length=15)
    number = PhoneNumberField()
    email = models.EmailField()
    password = models.CharField(max_length=30)
    profile_photo = models.ImageField(default='Brothers_cafe/static/images/download.jfif', upload_to='Brothers_cafe/images')
    cart = models.ManyToManyField(food, blank=True, null=True)
    
    def __str__(self):
        return self.fname
    
class contact_form(models.Model):
    fname = models.CharField(max_length=15)
    email = models.EmailField()
    message = models.TextField()
    
    def __str__(self):
        return self.fname
    
class Reservation(models.Model):
    name = models.CharField(max_length=30, default="")
    people = models.IntegerField(default=0)
    created_at = models.DateTimeField(default=datetime.datetime.now())
    
    def __str__(self):
        return self.name
    
# name - char field
# people - int field
# when - DateTime field

class Feedback(models.Model):
    name = models.CharField(max_length=30, default="")
    message = models.TextField(default="")
    rating = models.IntegerField(default=0)
    created_at = models.DateTimeField(default=datetime.datetime.now())







class GalleryCategory(models.Model):
    category_galery = models.CharField(max_length=30)
    
    def __str__(self):
        return self.category_galery
    
    
class GalleryImage(models.Model):
    image_name = models.CharField(max_length=100, null=True, blank=True)
    image_gallery = models.ImageField(null=True, blank=True, default="abcd.jpeg")
    categoryGalery = models.ForeignKey(GalleryCategory, on_delete=models.CASCADE, default="")
    def __str__(self):
        return self.image_name


class cart(models.Model):
    food_name = models.ForeignKey(food,on_delete=models.CASCADE,  blank=True, null=True)
    customer_name = models.ForeignKey(user_registration, on_delete=models.CASCADE,related_name="Customer_name")
    food_quantity = models.IntegerField(default=1)
    food_price = models.FloatField(default=0)
    total = models.FloatField(default=0, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
