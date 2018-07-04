from django.conf.urls import url
from accounts import views

app_name = 'accounts'

urlpatterns = [
    url(r'^register/$', views.register_member, name='register-member'),
    url(r'^login/$', views.login_view, name='login'),
    url(r'^logout/$', views.logout_view, name='logout'),
]