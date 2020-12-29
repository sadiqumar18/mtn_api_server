from django.conf.urls import url
from api import views

# Create your views here.




urlpatterns = [
    url(r'^api/buy_data', views.buy_data),
]