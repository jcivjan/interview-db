from django.conf.urls import url
from . import views

app_name = 'interview_db'
urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name="home"),
] 
