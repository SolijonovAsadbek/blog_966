from django.shortcuts import render, redirect, get_object_or_404

from blog import forms
from blog.forms import BlogForm
from blog.models import Blog


def home_view(request):
    blogs = Blog.objects.all()  # SELECT * FROM Blog;
    form = BlogForm()
    context = {
        'blogs': blogs,
        'form': form
    }
    return render(request, 'blog/home.html', context)


def create(request):
    if request.method == 'POST':
        form = BlogForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home-view')
        else:
            print(form.errors)
            return redirect('home-view')
    else:
        return redirect('home-view')


def detail(request, pk):
    blog = get_object_or_404(Blog, id=pk)
    form = BlogForm()
    context = {
        'blog': blog,
        'form': form
    }
    return render(request, 'blog/detail.html', context)
