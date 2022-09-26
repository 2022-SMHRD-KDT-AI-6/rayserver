from unicodedata import name
from django.urls import path
from .views import index, home_view, introcom_view, introrey_view, introteam_view

app_name = "home"

urlpatterns = [    
# 홈페이지
    path('', index, name=''),
    path('home', home_view, name='home'),
    path('introcom', introcom_view, name='introcom'),
    path('introrey', introrey_view, name='introrey'),
    path('introteam', introteam_view, name='introteam')
]
