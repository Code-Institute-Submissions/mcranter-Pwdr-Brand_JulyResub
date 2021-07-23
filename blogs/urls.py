from django.contrib import admin

# Register your models here.
from . import views
from django.urls import path

urlpatterns = [
    path("", views.post, name="blogs"),
    path("detail/<slug:slug>/", views.post_detail, name="post_detail"),
    path("add_blog/", views.add_post, name="add_post"),
    path("edit_blog/<slug:slug>/", views.edit_post, name="edit_post"),
    path("delete_blog/<slug:slug>/", views.delete_post, name="delete_post"),
]
