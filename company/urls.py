from django.conf.urls import url

from .views import (
    CompanyListAPIView,
    CompanyCreateAPIView,
    CompanyUpdateAPIView,
CompanyDeleteAPIView
)

urlpatterns = [
    url(r'^$', CompanyListAPIView.as_view(), name='list'),
    url(r'^create/$', CompanyCreateAPIView.as_view(), name='create'),
    url(r'^(?P<name>[\w-]+)/update/$', CompanyUpdateAPIView.as_view(), name='update'),
    url(r'^(?P<name>[\w-]+)/delete/$', CompanyDeleteAPIView.as_view(), name='delete'),
]
