from django.conf.urls import include
from django.urls import path
# from .views import MobileLogin, MobileRegist, ImageScore, MobileShowMember, ScoreData
from .views import *




urlpatterns = [
    # 어플
    # path('login', MobileLogin.as_view(), name='login'),
    path('', practice, name='')

]

