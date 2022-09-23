from django.conf.urls import include
from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name='fileup'),
    path('main2',views.main2),
    path('upload_success',views.upload_success),
    path('upload_success2',views.upload_success2),

]

