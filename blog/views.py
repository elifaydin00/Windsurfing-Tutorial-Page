from django.shortcuts import render
from datetime import date

all_posts=[
    {"slug":"hike-in-the-mountains",
    "image:":"mountains.jpg",
    "author":"Elif",
    "date": date(2021,8,2),
    "title": "Mountain Hiking",
    "excerpt":"The views were amazing while hiking. I will definitely do another hiking session",
    "content": "Some dummy paragraph blah blah blah blah blah blah blah blah blah blahblah dummy"},

    {"slug":"second-post",
    "image:":"ch.jpg",
    "author":"Elif",
    "date": date(2021,11,2),
    "title": "asdasdasdas",
    "excerpt":"experimental second post",
    "content": "Some dummy paragraph blah blah blah blah blah blah blah blah blah blahblah dummy"},

    {"slug":"third-post",
    "image:":"max.jpg",
    "author":"Elif",
    "date": date(2021,10,2),
    "title": "dasdasdasdasdasdasdasdasd",
    "excerpt":"experimental third post",
    "content": "Some dummy paragraph blah blah blah blah blah blah blah blah blah blahblah dummy"}
]

def get_date(post):
    return post['date']

# Create your views here.

def starting_page(request):
    sorted_posts=sorted(all_posts,key=get_date)
    latest_posts=sorted_posts[-3:]
    return render(request,"blog/index.html",
    {
        "posts":latest_posts
    })

def posts(request):
    return render(request,"blog/all-posts.html",
    {
        "all_posts":all_posts
    })

def post_detail(request,slug):
    return render(request,"blog/post-detail.html")

