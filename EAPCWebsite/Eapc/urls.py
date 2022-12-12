from django.urls import path
from . import views

"""in the Eapc.urls, the patterns index our views page"""
urlpatterns = [
    path("", views.index, name="index")
]