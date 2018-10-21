from django.conf.urls import url
from django.contrib.auth import views as auth_views
from . import views


app_name = 'accounts'

urlpatterns = [
    url(r'^$', views.dashboard, name='dashboard'),
    # url(r'^dashlog/$', views.dashboard_logout, name='dashboard_logout'),

    # url(r'^login/$', views.login_page, name='login'),
    url(r'^signup/$', views.signup_page, name='signup'),
    # url(r'^register/$', views.register_page, name='register'),
    # url(r'^logout/$', views.logout_view, name='logout'),

    url(r'^login/$', auth_views.LoginView.as_view(template_name='accounts/login_page.html'), name='login'),
    url(r'^logout/$', auth_views.LogoutView.as_view(), name='logout'),
]
