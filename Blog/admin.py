from django.contrib import admin
from .models import Article, Category, Message, Newsletter, Info, Comment, Profile
# Register your models here.
admin.site.register(Article)
admin.site.register(Category)
admin.site.register(Message)
admin.site.register(Newsletter)
admin.site.register(Info)
admin.site.register(Comment)
admin.site.register(Profile)
