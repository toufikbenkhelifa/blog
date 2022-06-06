from unicodedata import name
from django.urls import path
from .models import BlogPost
from .views import BlogPostUpdate, blogHome, BlogPostCreate , BlogPostDetail, BlogPostDelete

app_name="posts"

urlpatterns = [
    path('',blogHome.as_view(),name ='home'),
    path('create/',BlogPostCreate.as_view(),name='create'),
    path('<str:slug>/',BlogPostDetail.as_view(),name='details'),
    path('update/<str:slug>/',BlogPostUpdate.as_view(),name='update'),
    path('delete/<str:slug>/',BlogPostDelete.as_view(),name='delete'),

]
