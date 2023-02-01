from rest_framework import serializers
from .models import *

class foodSerializer(serializers.ModelSerializer):
    class Meta:
        model = food
        fields = "__all__"
        
        
class categorySerializer(serializers.ModelSerializer):
    class Meta:
        model = category_table
        fields = "__all__"