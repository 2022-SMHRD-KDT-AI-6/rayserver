from django.urls import path
from . import views


app_name = "predict"

urlpatterns = [    

# 예측테스트
    path('', views.home, name=''),
    path('predict', views.predict, name='predict'),
    path('result', views.result, name='result'),
    path('practice', views.practice, name='practice'),
    path('postcreate', views.postcreate, name='postcreate'),
    path('detail', views.detail, name='detail'),
    
    # path('upload',views.upload, name='upload'),
]
