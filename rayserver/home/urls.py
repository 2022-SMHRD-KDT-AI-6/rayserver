from django.urls import path
from .views import index, home_view

app_name = "home"

urlpatterns = [    
# 홈페이지
    path('', index, name=''),
    path('home', home_view, name='home')
]
