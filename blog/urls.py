from django.urls import path
from django.contrib.auth import views as auth_views
from .views import AddPost, PostList, PostDetail, PostLike, \
    UpdatePostView, DeletePostView, UserEditView, PasswordsChangeView
from . import views


urlpatterns = [
    path('', PostList.as_view(), name='home'),
    path('edit_profile/', UserEditView.as_view(), name='edit_profile'),
    path('password/', PasswordsChangeView.as_view(), name='change_password'),
    path('password_success', views.password_success, name='password_success'),
    path('like/<slug:slug>/', PostLike.as_view(), name='post_like'),

    path('add/', AddPost.as_view(), name='add_post'),
    
    path('<slug:slug>/', PostDetail.as_view(), name='post_detail'),
    path('edit/<slug:slug>/', UpdatePostView.as_view(), name='update_post'),
    path('<slug:slug>/delete/', DeletePostView.as_view(), name='delete'),
   
]