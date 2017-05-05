from django.conf.urls import url ,include
from django.contrib import admin

from .views import (
    UserLoginAPIView,
    UserCreateAPIView,
    UserProfileCreateAPIView,
    UserUpdateAPIView,
    UserProfileUpdateAPIView,
    UsersListAPIView
)

urlpatterns = [
    url(r'^$', UsersListAPIView.as_view(), name='all_users'),
    url(r'^login/$', UserLoginAPIView.as_view(), name='login'),
    # url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^register/$', UserCreateAPIView.as_view(), name='register'),
    url(r'^register_profile/$', UserProfileCreateAPIView.as_view(), name='register_profile'),
    url(r'^(?P<email>[\w@_\.]+)/update/$', UserUpdateAPIView.as_view(), name='update_user'),
    url(r'^(?P<user>[\d]+)/update_profile/$', UserProfileUpdateAPIView.as_view(), name='update_profile'),
]
