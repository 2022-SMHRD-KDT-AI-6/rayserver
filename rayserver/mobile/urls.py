from django.conf.urls import include
from django.urls import path
from .views import GameSave, MobileLogin, MobileRegist, ImageScore, MobileShowMember, ScoreData, GameScoreShow


from . import views

urlpatterns = [
    # 어플
    path('login', MobileLogin.as_view(), name='login'),
    path('regist', MobileRegist.as_view(), name='regist'),
    path('score', ImageScore.as_view(), name='score'),
    path('scoredata', ScoreData.as_view(), name='scoredata'),
    path('showmember', MobileShowMember.as_view(), name='showmember'),

    path('gamescore',GameScoreShow.as_view(), name='gamescore'),
    path('gamesave', GameSave.as_view(), name='gamesave'),
]

