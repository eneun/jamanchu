from django.urls import path
from . import views

urlpatterns = [
    path('scraplist/', views.scraplist, name="scraplist"),
]
