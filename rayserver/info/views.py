import code
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from requests import Response
from .models import FoodTable
from django.core import serializers
from rest_framework.views import APIView
from predict.models import ImgSave
from .serializer import FoodSerializer
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def foodinfo(request):
    if request.method == 'GET':
        query_set = FoodTable.objects.all()
        serializer = FoodSerializer(query_set, many=True)
        return JsonResponse(serializer.data, safe=False)