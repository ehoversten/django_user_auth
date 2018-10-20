from django.conf.urls import url
from . import views


app_name = 'accounts'

urlpatterns = [
    url(r'^$', views.dashboard, name='dashboard'),
    url(r'^dashlog/$', views.dashboard_logout, name='dashboard_logout'),

    url(r'^login/$', views.login_page, name='login'),
    url(r'^signup/$', views.signup_page, name='signup'),
    # url(r'^register/$', views.register_page, name='register'),
    url(r'^logout/$', views.logout_view, name='logout'),
]
