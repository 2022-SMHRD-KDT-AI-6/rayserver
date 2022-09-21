from django.urls import path
from .views import index

app_name = "home"

urlpatterns = [    
# 홈페이지
    path('', index, name=''),
]
