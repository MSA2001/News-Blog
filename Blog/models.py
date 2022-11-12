from django.contrib.auth.models import User
from django.db import models

# Create your models here.


class Category(models.Model):
    title = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "categories"

    def __str__(self):
        return self.title


class Article(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ManyToManyField(Category, related_name='articles')
    title = models.CharField(max_length=100)
    body = models.TextField(max_length=2000)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='profile/image', blank=True, null=True)

    def __str__(self):
        return self.title


class Message(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField(max_length=50)
    title = models.CharField(max_length=85)
    body = models.TextField(max_length=750)

    def __str__(self):
        return self.title


class Newsletter(models.Model):
    email = models.EmailField(max_length=35)

    def __str__(self):
        return self.email


class Info(models.Model):
    body = models.CharField(max_length=200, null=True, blank=True)
    location = models.CharField(max_length=200, null=True, blank=True)
    number = models.IntegerField(max_length=20, null=True, blank=True)
    email = models.EmailField(max_length=30, null=True, blank=True)
    site = models.CharField(max_length=30, null=True, blank=True)


