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
# 장고 디버깅
from django.conf.urls import url, include
from django.conf import settings

import home.views
import meeting.views
import accounts.views
import profiles.views
import message.views
import scrap.views

urlpatterns = [
    # 관리자 페이지
    path('admin/', admin.site.urls),
    # 메인 페이지
    path('', accounts.views.login, name="login"),
    # home 앱
    path('home/', include('home.urls')),
    # meeting 앱
    path('meeting/', include('meeting.urls')),
    # accounts 앱
    path('accounts/', include('accounts.urls')),
    # profiles 앱
    path('profiles/', include('profiles.urls')),
    # message 앱
    path('message/', include('message.urls')),
    # search 앱
    path('search/', include('search.urls')),
    # scrap 앱
    path('scrap/', include('scrap.urls')),
]

# if settings.DEBUG:
#     import debug_toolbar
#     urlpatterns += [
#         url(r'^__debug__/', include(debug_toolbar.urls)),
# ]