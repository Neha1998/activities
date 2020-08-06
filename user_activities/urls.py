from django.conf.urls import url
from user_activities import views

urlpatterns = [
    url(r'^get_users/$', views.get_users),
]