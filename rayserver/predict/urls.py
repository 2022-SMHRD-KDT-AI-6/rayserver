from django.urls import path
from . import views


app_name = "predict"

urlpatterns = [    

# 예측테스트
    # path('', views.home, name=''),
    path('', views.StoreView.as_view(), name="store"),
    path('product/<int:pk>/', views.ProductDetailView.as_view(), name="product_detail"),
    path('predict', views.predict, name='predict'),
    path('result', views.result, name='result'),
    path('practice', views.practice, name='practice'),
    path('postcreate', views.postcreate, name='postcreate'),
    # path('detail', views.detail, name='detail'),
    
    path('imgtest', views.imgtest, name='imgtest'),
    path('scoretest', views.scoredata2, name='scoretest'),
    
    # path('upload',views.upload, name='upload'),
]
