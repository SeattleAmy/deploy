from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^$', views.index),
    url(r'^create$', views.create),
    url(r'^success$', views.success),
    url(r'^emails/(?P<id>[0-9]*)/delete', views.destroy)
]
