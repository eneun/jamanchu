from django.urls import path
from . import views

urlpatterns = [
    path('filters/', views.filters, name="filters"),
    path('result/', views.result, name="result"),
]
