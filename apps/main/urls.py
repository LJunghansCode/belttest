from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^create/$', views.create, name='create'),
    url(r'^delete/$', views.delete_appointment, name="delete"),
    url(r'^appointment/(?P<apt_id>\d+)$', views.edit, name="edit"),
    url(r'^edit/', views.edit_appointment, name="editAppointment"),


    ]