from django.conf.urls import url
from admin.myRNN import views

urlpatterns={
    url(r'ram', views.ram_price),
    url(r'kia', views.kia_predict),
}