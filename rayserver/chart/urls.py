from django.urls import path
from . import views


app_name = "chart"

urlpatterns = [    

# 예측테스트
    # path('', views.home, name=''),
    # path('', views.StoreView.as_view(), name="store"),
    path('', views.chartShow, name='chart'),
    path('chart3', views.chart_bar3, name='chart3'),
    path('chartview', views.ChartView.as_view(), name='chartview')
]