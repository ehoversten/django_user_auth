from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.dashboard, name='dashboard'),
    url(r'^login/$', views.login_page, name='login'),
    url(r'^register/$', views.register_page, name='register')
]
