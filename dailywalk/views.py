from django.shortcuts import render
from .models import Blog
from django.utils import timezone


# Create your views here.


def index(request):
    blog = Blog.objects.filter(created_date__lte=timezone.now()).order_by('created_date')
    return render(request, "dailywalk/home.html", {'blogs': blog})
