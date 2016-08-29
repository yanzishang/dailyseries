from django.db import models
from __future__ import unicode_literals
from django.utils.encoding import python_2_unicode_compatible
# Create your models here.

@python_2_unicode_compatible
class Column(models.Model):
    name = models.CharField('栏目名称',max_length=256)
    slug = models.CharField('栏目网址',max_length=256,db_index=True)
    intro = models.TextField('栏目简介',default='')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '栏目'
        verbose_name_plural = '栏目'
        ordering = ['name']


# http://www.ziqiangxuetang.com/django/django-cms-develop.html

class Article(models.Model):
    column = models.ManyToManyField(Column,verbose_name='归属栏目')
    