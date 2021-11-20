from django.conf.urls import url
from admin.iris import views

urlpatterns = {
    url(r'base', views.base),
    url(r'advance', views.advance),
    url(r'tf', views.advance),

}