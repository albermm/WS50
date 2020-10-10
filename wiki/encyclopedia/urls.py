from django.urls import path, re_path
from . import views


app_name = "wiki"
urlpatterns = [
    path("", views.index, name="index"),
    path("<str:title>", views.title, name="title"),
    path("error/", views.title, name="error"),
    path("results/", views.search, name="results")

    
   ]
