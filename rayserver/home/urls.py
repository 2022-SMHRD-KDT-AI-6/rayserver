from unicodedata import name
from django.urls import path
from .views import imgresult_view, index, home_view, introcom_view, introrey_view, introteam_view,ChartView, chart_view

app_name = "home"

urlpatterns = [    
# 홈페이지
    path('test', index, name='test'),
    path('home', home_view, name='home'),
    path('introcom', introcom_view, name='introcom'),
    path('introrey', introrey_view, name='introrey'),
    path('introteam', introteam_view, name='introteam'),
    path('view',ChartView.as_view(),name='view'),
    path('imgresult', imgresult_view, name='imgresult'),
    path('', chart_view, name='')
]
