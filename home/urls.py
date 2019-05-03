from django.urls import path
from . import views

urlpatterns = [
    path('second/', views.second, name="second"),
    path('third/', views.third, name="third"),
]
