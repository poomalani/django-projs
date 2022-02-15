from django.conf.urls import url
from FinSolvers_App1 import views

app_name='FinSolvers_App1'

urlpatterns=[
    url(r'^register/$', views.register,name='register'),
    url(r'^user_login/$', views.user_login,name='user_login')
]