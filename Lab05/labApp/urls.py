from django.urls import path
from . import views

urlpatterns = [
    path('', views.display, name="show"),
    path('add', views.add, name="add")
]