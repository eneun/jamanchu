from django.urls import path
from . import views

urlpatterns = [
    path('listmessage/', views.listmessage, name="listmessage"),
    path('new/<int:meeting_id>/', views.new, name="newmessage"),
    path('create/<int:meeting_id>/', views.create, name="createmessage"),
    path('show/', views.show, name="showmessage"),
]
