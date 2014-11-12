from django.conf.urls import patterns, url
from . import views


urlpatterns = patterns(
    "",
    url(r"^$", views.index, name="index"),
    url(r"^(?P<contact_id>\d+)/$", views.show, name="show"),
    url(r"^(?P<contact_id>\d+)/edit/$", views.edit, name="edit"),
)
