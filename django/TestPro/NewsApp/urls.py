# This is copied from main
from django.urls import path, include
from .views import  News

urlpatterns = [
    path('news/', News, name = "News"),
]
