from django.conf.urls import include
from django.urls import path
# from .views import MobileLogin, MobileRegist, ImageScore, MobileShowMember, ScoreData
from .views import *
from .views import foodinfo, trainInfo, columnInfo, practice




urlpatterns = [
    # 어플
    path('food', foodinfo, name='food'),
    path('train', trainInfo, name='train'),
    path('column', columnInfo, name='column'),
    path('allinsert',practice,name='allinsert')

]

