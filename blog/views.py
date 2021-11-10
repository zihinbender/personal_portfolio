from django.shortcuts import render
from blog.models import Post, Comment
from .forms import CommentForm

# Create your views here.

def blog_index(request):
    posts = Post.objects.all().order_by('-created_on')
    
    return render(request, "blog/blog_index.html", {
        'posts' : posts
    })

def blog_category(request, category):
    posts = Post.objects.filter(
        categories__name__contains = category
    ).order_by('-created_on')
    
    return render(request, "blog/blog_category.html", {
        'category' : category,
        'posts' : posts
    })

def blog_detail(request, pk):
    post = Post.objects.get(pk=pk)
    comments = Comment.objects.filter(post=post)

    form = CommentForm()
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = Comment(
                author = form.cleaned_data["author"],
                body = form.cleaned_data["body"],
                post = post            
            )
            comment.save()

    

    return render(request, "blog/blog_detail.html", {
        'post' : post,
        'comments' : comments,
        'form' : form
    })