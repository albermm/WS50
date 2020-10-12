from django.urls import path, re_path
from . import views


app_name = "encyclopedia"
urlpatterns = [
    path("", views.index, name="index"),
    path("<str:title>", views.title, name="title"),
    path("error/", views.title, name="error"),
    path("edit/", views.edit, name="edit"),
    path("add/",  views.add, name="add")
  
   ]
