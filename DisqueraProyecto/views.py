from django.shortcuts import render, get_object_or_404, redirect

from .models import Post, Category
from .forms import CommentForm


def home(request):
   posts = Post.objects.filter(status=Post.ACTIVE).order_by('-created_at')

   context = {
       'posts': posts
   }

   return render(request, 'disquera/home.html', context)


def detail(request, id):
   post = get_object_or_404(Post, id=id, status=Post.ACTIVE)

   if request.method == 'POST':
       form = CommentForm(request.POST)

       if form.is_valid():
           comment = form.save(commit=False)
           comment.post = post
           comment.save()

           return redirect('post_detail', id=id)

   else:
       form = CommentForm()

   context = {
       'post': post,
       'form': form
   }

   return render(request, 'disquera/detail.html', context)
