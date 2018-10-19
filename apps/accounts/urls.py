from django.conf.urls import url
from . import views


app_name = 'accounts'

urlpatterns = [
    url(r'^$', views.dashboard, name='dashboard'),
    url(r'^login/$', views.login_page, name='login'),
    url(r'^register/$', views.register_page, name='register')
]
