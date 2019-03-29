from django.urls import path
from . import views

urlpatterns = [
    path('listpage/', views.listpage, name="listpage"),
    path('<int:meeting_id>/', views.detail, name="detail"),
]
