from django.urls import path 
from . import views

urlpatterns = [
    path('', views.home, name='home'), 
    path('detail/<str:pk>/', views.detail, name='detail'),
    path('create/', views.create, name='create'),
    path('update/<str:pk>', views.update, name='update'),
    path('delete/<str:pk>/', views.delete_blog, name='delete'),
    path('search/', views.search, name='search'),
    path('detail_search/', views.detail_search, name='detail_search'),
    path('register/', views.register_user, name='register'),
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),

]