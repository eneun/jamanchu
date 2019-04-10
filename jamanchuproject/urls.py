"""jamanchuproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
import home.views
import meeting.views
import accounts.views

urlpatterns = [
    # 관리자 페이지
    path('admin/', admin.site.urls),
    # 메인 페이지
    path('', home.views.index, name="index"),
    # home 앱
    path('home/', include('home.urls')),
    # meeting 앱
    path('meeting/', include('meeting.urls')),
    # accounts 앱
    path('accounts/', include('accounts.urls')),
]
