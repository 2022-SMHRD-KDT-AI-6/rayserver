from django.conf.urls import include
from django.urls import path

from .views import PostViewSet
from .views import CommentViewSet
from . import views

urlpatterns = [
    # path('', views.index, name='index'),
    path('', views.list, name='list'),
    path('create/', views.create, name='create'),
    path('post', PostViewSet.as_view({'get':'list', 'post':'create'})),
    path('comment', CommentViewSet.as_view({'get':'list', 'post':'create'})),
]

