from django.contrib import admin
from .models import Article, Category, Message
# Register your models here.
admin.site.register(Article)
admin.site.register(Category)
admin.site.register(Message)
