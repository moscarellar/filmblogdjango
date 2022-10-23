from . import views
from django.urls import path
from django.contrib.auth import views as auth_views
from .views import PostList, PostDetail, PostLike

urlpatterns = [
    path('', views.PostList.as_view(), name='home'),
    path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
    path('like/<slug:slug>', views.PostLike.as_view(), name='post_like'),
    path('<slug:slug>/', PostDetail.as_view(), name='post_detail'),
    
]
