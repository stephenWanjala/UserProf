from django.urls import path

from userprofile import views

urlpatterns = [
    path('create/', views.create_profile, name='create_profile'),
    path('user/<int:pk>/', views.user_detail, name='user_detail'),
    path('', views.profile_list, name='profile_list'),
]
