from django.shortcuts import render, get_object_or_404
from postapp.models import Post

# Create your views here.

def home(request):

    return render(request,'postapp/home.html')


def post_lists(request):
    posts = Post.objects.all().order_by('-time')  # here order_by('-time') means in frontend letest value came.
    return render(request,'postapp/post_lists.html', {'posts':posts})



def post_detail(request,slug):
    post = get_object_or_404(Post, slug=slug)
    return render(request,'postapp/post_detail.html', {'post':post})