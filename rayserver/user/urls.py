from django.urls import path
from .views import UserRegist, UserLogin, home_view, MobileLogin, MobileRegist

app_name = "user"

urlpatterns = [    
    path('', home_view, name=''),
    path('user_login', UserLogin.as_view(), name='user_login'),
    path('user_regist', UserRegist.as_view(), name='user_regist'),

    path('m_login',MobileLogin.as_view(), name='m_login'),
    path('m_regist',MobileRegist.as_view(), name='m_regist'),
]
