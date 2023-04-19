from django.urls import path
from . import views

urlpatterns = [
    path("", views.ViewPosts, name='home'),
    path("like/<int:pk>", views.like_post, name="like_post"),
    path("comment/<int:pk>", views.ShowComments,name="comment"),
    path("addcomment/<int:pk>", views.addComment, name ="addcomment"),
    path("addpost/",views.addPost,name="addpost"),
    path("postdetails/<int:pk>", views.PostDetails, name="postdetails"),

]