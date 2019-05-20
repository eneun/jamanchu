from django.urls import path
from . import views

urlpatterns = [
    path('scraplist/', views.scraplist, name="scraplist"),
    path('scrap/<int:meeting_id>', views.scrap, name="scrap"),
]
