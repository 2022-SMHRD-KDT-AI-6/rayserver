from unicodedata import name
from django.urls import path
from .views import imgresult_view, index, home_view, introcom_view, introrey_view, introteam_view,ChartView, chart_bar3

app_name = "home"

urlpatterns = [    
# 홈페이지
    path('', index, name=''),
    path('home', home_view, name='home'),
    path('introcom', introcom_view, name='introcom'),
    path('introrey', introrey_view, name='introrey'),
    path('introteam', introteam_view, name='introteam'),
    path('view',ChartView.as_view(),name='view'),
    path('imgresult', imgresult_view, name='imgresult'),
    path('test', chart_bar3, name='test')
]
