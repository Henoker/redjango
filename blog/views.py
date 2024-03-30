from django.shortcuts import render
from django.utils import timezone
from blog.models import Post
from django.shortcuts import render, get_object_or_404
from blog.forms import CommentForm
from django.shortcuts import redirect



# Create your views here.
def index(request):
    posts = Post.objects.filter(published_at__lte=timezone.now())
    return render(request, "blog/index.html", {"posts": posts})

def post_detail(request, slug):
    post = get_object_or_404(Post, slug=slug)
    if request.user.is_active:
        if request.method == "POST":
            comment_form = CommentForm(request.POST)
<<<<<<< HEAD
=======
            
>>>>>>> c2ac073 (feat: add forms.py comment form)
            if comment_form.is_valid():
                comment = comment_form.save(commit=False)
                comment.content_object = post
                comment.creator = request.user
                comment.save()
                return redirect(request.path_info)
<<<<<<< HEAD
            else:
                comment_form = CommentForm()
        else:
            comment_form = None
    return render(request, "blog/post-detail.html", {"post":post, comment_form:comment_form})
=======
        else:
            comment_form = CommentForm()
    else:
        comment_form = None
    return render(request, "blog/post-detail.html", {"post":post, comment_form: comment_form})
>>>>>>> c2ac073 (feat: add forms.py comment form)
