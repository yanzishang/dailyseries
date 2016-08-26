from django.shortcuts import render, get_object_or_404, redirect
from .models import Blog
from django.utils import timezone
from .forms import BlogForm


# Create your views here.


def index(request):
    blog = Blog.objects.filter(created_date__lte=timezone.now()).order_by('created_date')
    return render(request, "dailywalk/home.html", {'blogs': blog})


def blog_detail(request, pk):
    blog = get_object_or_404(Blog, pk=pk)
    return render(request, 'dailywalk/blog_detail.html', {'blog': blog})


def blog_new(request):
    if request.method == "POST":
        form = BlogForm(request.POST)
        if form.is_valid():
            blog = form.save(commit=False)
            blog.author = request.user
            blog.created_date = timezone.now()
            blog.save()
            return redirect('dailywalk.views.blog_detail', pk=blog.pk)
    else:
        form = BlogForm()
        return render(request, 'dailywalk/blog_edit.html', {'form': form})


def blog_edit(request, pk):
    blog = get_object_or_404(Blog, pk=pk)
    if request.method == "POST":
        form = BlogForm(request.POST, instance=blog)
        if form.is_valid():
            blog = form.save(commit=False)
            blog.author = request.user
            blog.created_date = timezone.now()
            blog.save()
            return redirect('dailywalk.views.blog_detail', pk=blog.pk)
    else:
        form = BlogForm(instance=blog)
    return render(request, 'dailywalk/blog_edit.html', {'form': form})
