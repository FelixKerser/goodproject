from django.urls import path
from . import views

urlpatterns = [
    path('', views.info_site, name='info_site'),
]