from django.urls import path
from . import views


urlpatterns = [
    path('', views.base, name='base'),
    path('register/', views.register_user, name="register_user"),
    path('login/', views.Login_user, name="login"),
    path('login_store', views.Login_store),
    path('logout/', views.Logout_user),
    path('form/', views.form, name="form"),
    path('post_list/', views.posts_list, name="posts"),
    path('posts/<int:pk>/', views.post_detail, name="post_detail"),
    path('profile/', views.profile, name="profile"),
    path('reports/', views.reports, name="reports"),
    path('post_delete/<int:pk>/', views.post_delete, name="post_delete"),
    path('post_update/update/<int:pk>/', views.post_update, name="post_update"),
    path('found_create/', views.found_create, name="found"),
    path('found_update/updated/<int:pk>/', views.found_update, name="found_update"),
    path('found_delete/<int:pk>/', views.found_delete, name="found_delete"),
]