from django.conf.urls import url
from views import index, login, register, logout
from . import views
urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'^login$', login, name='login'),
    url(r'^register$', register, name='register'),
    url(r'^logout$', logout, name='logout'),
]
