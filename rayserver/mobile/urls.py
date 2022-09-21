from django.conf.urls import include
from django.urls import path
from .views import MobileLogin, MobileRegist


from . import views

urlpatterns = [
    # 어플
    path('login', MobileLogin.as_view(), name='login'),
    path('regist', MobileRegist.as_view(), name='regist'),
]

