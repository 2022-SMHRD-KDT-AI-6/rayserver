from rest_framework import serializers
from .models import FoodTable3, TrainingTable3, ColumnTable

class FoodSerializer(serializers.ModelSerializer):
    class Meta:
        model = FoodTable3
        fields = ['food_title','food_info','food_img']
        
class TrainingSerializer(serializers.ModelSerializer):
    class Meta:
        model = TrainingTable3
        fields = ['train_title','train_info','train_img']

class ColumnSerializer(serializers.ModelSerializer):
    class Meta:
        model = ColumnTable
        fields = ['column_title','column_content','column_img','column_link']
