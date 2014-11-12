from django.conf.urls import patterns, url
from . import views


urlpatterns = patterns(
    "",
    url(r"^$", views.index, name="index"),
    url(r"^data/$", views.Data.as_view(), name="data"),
    url(r"^(?P<pk>\d+)/$", views.Show.as_view(), name="show"),
    url(r"^add/$", views.edit, name="show"),
    url(r"^(?P<contact_id>\d+)/edit/$", views.edit, name="edit"),
)
