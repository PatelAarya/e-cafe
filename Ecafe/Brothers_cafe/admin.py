from django.contrib import admin
from .models import *

# Register your models here.

admin.site.register(user_registration)
admin.site.register(contact_form)
admin.site.register(category_table)
admin.site.register(food)
admin.site.register(GalleryImage)
admin.site.register(Feedback)
admin.site.register(Reservation)
admin.site.register(GalleryCategory)
admin.site.register(cart)



