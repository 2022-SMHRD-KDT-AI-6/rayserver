from rest_framework import serializers
from .models import FoodTable

class FoodSerializer(serializers.ModelSerializer):
    class Meta:
        model = FoodTable
        fields = ['food_info','food_img']
        
