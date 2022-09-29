from django.http import HttpResponse
from django.shortcuts import render
from .models import FoodTable

# Create your views here.
def practice(request):
    print('a')
    queryset = FoodTable.objects.all()
    print(queryset[1])
    return HttpResponse(status=200)
