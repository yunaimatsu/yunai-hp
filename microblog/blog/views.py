from django.shortcuts import redirect, render
from blog.forms import CommentForm
from .models import Post

# define "frontpage" view
def frontpage(request):
    # get all obejects in DB
    posts = Post.objects.all()
    return render(request, "blog/frontpage.html", {"posts": posts})

# define "post_detail" view
def post_detail(request, slug):
    post = Post.objects.get(slug=slug)
    
    # post or comment?
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            
            return redirect("post_detail", slug=post.slug)
    else:
        form = CommentForm()
        
    return render(request, "blog/post_detail.html", {"post": post, "form": form})
