from django.urls import path
from . import views

urlpatterns = [
    path('mypage/', views.mypage, name="mypage"),
    path('new/', views.new, name="newprofile"),
    path('profilecreate/', views.profilecreate, name="profilecreate"),
    path('mymeeting/', views.mymeeting, name="mymeeting"),
]