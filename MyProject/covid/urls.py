from . import views
from django.urls import path

urlpatterns = [
    path('', views.index, name='index'),
    path('list/', views.countrylist, name='clist'),
    path('line/', views.lineplot, name='lineplot'),
    ]