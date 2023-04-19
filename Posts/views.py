from django.shortcuts import render, redirect
from .models import BlogPost, Comments
from .forms import CommentsForm
from Account.models import User


def ViewPosts(request):
    all_posts = BlogPost.objects.all()
    cforms = CommentsForm()
    context= {
        'all_posts' : all_posts,
        'all_users' : User.objects.all()
    }
    return render( request, "Account/homepage.html", context)


def like_post(request, pk):
    post = BlogPost.objects.get(id=pk)
    user = request.user
    if user in post.likes.all():
        post.likes.remove(user)
        liked = False
    else:
        post.likes.add(user)
        liked = True
    context = {
        'liked': liked,
    }
    return redirect("home")

def ShowComments(request,pk):
    comments = BlogPost.objects.filter(post=pk).all()
    return render(request,"Account/homepage.html")

def addComment(request,pk):
    if request.method=='POST':
        post = BlogPost.objects.get(id=pk)
        comment = request.POST.get("usercomment")
        print(comment)
        obj = Comments.objects.create(user=request.user, text=comment,post=post)
        obj.save()
        return redirect("home")
    else:
        print("no post request")
        return redirect("home")

def addPost(request):
    if request.method =="POST":
        cap = request.POST.get("caption")
        image =request.FILES["images"]
        print(image)
        
        post = BlogPost.objects.create(user=request.user, caption=cap, images=image)
        post.save()
        return redirect("home")
    else:
        return redirect("home")

def PostDetails(request, pk):
    posts = BlogPost.objects.get(id=pk)
    comments = Comments.objects.filter(post=posts)
    context={
        "post": posts,
        'comments':comments,
        'all_users' : User.objects.all(),
    }
    return render(request, 'Account/postdetails.html', context)