from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Column, Article


# Create your views here.
def index(request):
    home_display_columns = Column.objects.filter(home_display=True)
    nav_display_columns = Column.objects.filter(nav_display=True)
    return render(request, 'dailynews/index.html', {
        'home_display_columns': home_display_columns,
        'nav_display_columns': nav_display_columns
    })
    # columns = Column.objects.all()
    # return render(request, 'dailynews/index.html', {'columns': columns})


def column_detail(request, column_slug):
    column = Column.objects.get(slug=column_slug)
    return render(request, 'dailynews/column.html', {'column': column})


def article_detail(request, pk, article_slug):
    article = Article.objects.get(pk=pk)
    if article_slug != article.slug:
        return redirect(article, permanent=True)

    return render(request, 'dailynews/article.html', {'article': article})
