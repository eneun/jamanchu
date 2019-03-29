from django.urls import path
from . import views

urlpatterns = [
    path('listpage/', views.listpage, name="listpage"),
]
