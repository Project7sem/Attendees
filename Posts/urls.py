from django.urls import path
from . import views

urlpatterns = [
    path("", views.ViewPosts, name='home'),
    path("like/<int:pk>", views.like_post, name="like_post"),
    path("comment/<int:pk>", views.ShowComments,name="comment"),
    path("addcomment/<int:pk>", views.addComment, name ="addcomment"),

]