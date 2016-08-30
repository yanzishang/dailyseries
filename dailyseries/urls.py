"""dailyseries URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from dailywalk import views as dailywalk_views
from dailynews import views as dailynews_views
from dailyseries import views as dailyseries_views
from django.conf import settings

from DjangoUeditor import urls as DjangoUeditor_urls

urlpatterns = [
    url(r'^$', dailyseries_views.index, name='index'),
    url(r'^dailywalk/', dailywalk_views.index, name='dailywalk_index'),
    url(r'^blog/(?P<pk>[0-9]+)/$', dailywalk_views.blog_detail, name='blog_detail'),
    url(r'^blog/new/$', dailywalk_views.blog_new, name='blog_new'),
    url(r'^blog/(?P<pk>[0-9]+)/edit/$', dailywalk_views.blog_edit, name='blog_edit'),
    url(r'^admin/', admin.site.urls),
    url(r'^ueditor/', include(DjangoUeditor_urls)),
    url(r'^dailynews/', dailynews_views.index, name='dailynews_index'),
    url(r'^column/(?P<column_slug>[^/]+)/$', dailynews_views.column_detail, name='column'),
    url(r'^news/(?P<article_slug>[^/]+)/$', dailynews_views.article_detail, name='article'),
]

if settings.DEBUG:
    from django.conf.urls.static import static

    urlpatterns += static(
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT
    )
