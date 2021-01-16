from django.conf.urls import url
from api import views

# Create your views here.


urlpatterns = [
  url(r'^api/buy_data', views.cooperate_data),
  url(r'^api/login', views.browser_login),
  url(r'^api/refresh', views.refresh)
]
