from django.urls import path
from . import views

urlpatterns=[
    path("",views.starting_page,name="starting-page"), #introduction page where you can see latests posts and can direct to /posts
path("posts", views.posts,name="posts-page"), #/posts where you can see all the posts
path("posts/<slug:slug>",views.post_detail,name="post-detail-page")] #/posts/my-first-post