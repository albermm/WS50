from django.urls import path
from . import views


app_name = "wiki"
urlpatterns = [
    path("", views.index, name="index"),
    path("<str:title>", views.title, name="title"),
    path("error/", views.title, name="error"),
    path("add/", views.add, name="add")
   ]
