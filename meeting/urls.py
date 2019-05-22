from django.urls import path
from . import views

urlpatterns = [
    path('listpage/', views.listpage, name="listpage"),
    path('<int:meeting_id>/', views.detail, name="detail"),
    path('new/', views.new, name="new"),
    # path('create/', views.create, name="create"),
    path('meetingcreate/', views.meeting_new, name="meetingcreate"),
    path('edit/', views.edit, name='edit'),
    path('meetingupdate/<int:meeting_id>', views.meeting_update, name="meetingupdate"),
    path('meetingdestroy/<int:meeting_id>', views.meeting_destroy, name="meetingdestroy"),
]
