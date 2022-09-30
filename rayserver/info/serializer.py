from rest_framework import serializers
from .models import FoodTable, TrainingTable, ColumnTable

class FoodSerializer(serializers.ModelSerializer):
    class Meta:
        model = FoodTable
        fields = ['food_info','food_img']
        
class TrainingSerializer(serializers.ModelSerializer):
    class Meta:
        model = TrainingTable
        fields = ['train_info','train_img']

class ColumnSerializer(serializers.ModelSerializer):
    class Meta:
        model = ColumnTable
        fields = ['column_title','column_content','column_img','column_link']
