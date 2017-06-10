from django.db import models
from django.contrib import admin
import datetime
# Create your models here.
class Article(models.Model):
    title = models.CharField(null=True,blank=True,max_length=500)
    comment = models.TextField(null=True)
    abstract = models.TextField(null=True)
    body = models.TextField(null=True)
    create_time = models.DateTimeField(blank=True,default=datetime.datetime.now)
    category = models.ForeignKey('Category',verbose_name='Tag',null=True,blank=True,)
    VOTE_CHOICES = (
        ('Draft', 'Draft'),
        ('Complete', 'Complete'),
    )
    Status = models.CharField(choices=VOTE_CHOICES, max_length=10)

    def __str__(self):
        return self.title


class Category(models.Model):
    name = models.CharField(max_length=20)
    create_time = models.DateTimeField(blank=True, default=datetime.datetime.now)

    def __str__(self):
        return self.name

class Link(models.Model):
    name = models.CharField(max_length=32, unique=True)
    url = models.URLField(unique=True)
    description = models.CharField(max_length=255, default='此用户没有添加任何描述')
    add_time = models.DateTimeField(blank=True,default=datetime.datetime.now)
    def __str__(self):
        return self.name