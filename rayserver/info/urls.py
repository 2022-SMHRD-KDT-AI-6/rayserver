from django.conf.urls import include
from django.urls import path
# from .views import MobileLogin, MobileRegist, ImageScore, MobileShowMember, ScoreData
from .views import *
from .views import foodinfo




urlpatterns = [
    # 어플
    path('food', foodinfo, name='food')

]

