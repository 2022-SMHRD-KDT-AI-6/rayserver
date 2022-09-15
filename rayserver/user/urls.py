from django.urls import path
from .views import UserRegist, UserLogin, MobileLogin, MobileRegist
from .views import home_view, signup_view, login_view

app_name = "user"

urlpatterns = [    
    path('', home_view, name=''),
    path('signup', signup_view, name='signup'),
    path('raylogin', login_view, name='raylogin'),

    path('user_login', UserLogin.as_view(), name='user_login'),
    path('user_regist', UserRegist.as_view(), name='user_regist'),

    path('m_login', MobileLogin.as_view(), name='m_login'),
    path('m_regist', MobileRegist.as_view(), name='m_regist'),
]
