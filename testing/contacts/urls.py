from django.conf.urls import patterns, url
from . import views


urlpatterns = patterns(
    "",
    url(r"^$", views.index, name="index"),
    url(r"^data/$", views.Data.as_view(), name="data"),
    url(r"^(?P<contact_id>\d+)/$", views.show, name="show"),
    url(r"^add/$", views.show, name="show"),
    url(r"^(?P<contact_id>\d+)/edit/$", views.edit, name="edit"),
)
