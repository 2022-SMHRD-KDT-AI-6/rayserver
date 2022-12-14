import code
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from requests import Response
from .models import FoodTable3, TrainingTable3, ColumnTable
from django.core import serializers
from rest_framework.views import APIView
from predict.models import ImgSave
from .serializer import ColumnSerializer, FoodSerializer, TrainingSerializer
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import CreateView

@csrf_exempt
def foodinfo(request):
    if request.method == 'POST':
        query_set = FoodTable3.objects.all()
        serializer = FoodSerializer(query_set, many=True)
        return JsonResponse(serializer.data, safe=False)

@csrf_exempt
def trainInfo(request):
    if request.method == 'POST':
        query_set = TrainingTable3.objects.all()
        serializer = TrainingSerializer(query_set, many=True)
        return JsonResponse(serializer.data, safe=False)

@csrf_exempt
def columnInfo(request):
    if request.method == 'POST':
        query_set = ColumnTable.objects.all()
        serializer = ColumnSerializer(query_set, many=True)
        return JsonResponse(serializer.data, safe=False)
import os
from datetime import datetime
from django.urls import reverse_lazy

BASE_DIR = "C:/Users/smhrd/Desktop/"
img_files = os.path.join(BASE_DIR,'img/')


def practice(request):
    print(img_files)
    return HttpResponse('Hello world!')


class trainInfoOne(APIView):
    def post(self, request):
        print("로그 : " +str(request.body))
        class_object = TrainingTable3.objects.filter(train_seq='1').first()
        data = dict(
            msg="운동데이터하나", 
            code="200"
            )
        return Response(data)