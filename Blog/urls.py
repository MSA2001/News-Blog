from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.home, name='home'),
    path('lifestyle/', views.cat_lifestyle, name='cat_lifestyle'),
    path('technology/', views.cat_tech, name='cat_tech'),
    path('travel/', views.cat_travel, name='cat_travel'),
    path('contact/', views.contact, name='contact'),
    path('login/', views.signin, name='signin'),
    path('register/', views.register, name='register'),
    path('logout/', views.user_logout, name='logout'),
]