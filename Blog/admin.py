from django.contrib import admin
from .models import Article, Category, Message, Newsletter
# Register your models here.
admin.site.register(Article)
admin.site.register(Category)
admin.site.register(Message)
admin.site.register(Newsletter)
