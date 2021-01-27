from django.urls import path     
from .views import (
    PostListView, 
    PostDetailView, 
    PostCreateView,
    PostUpdateView,
    PostDeleteView,
    UserPostListView,
)

from . import views

urlpatterns = [
    path('', PostListView.as_view(), name='blog_home'),
    path('user/<str:username>/', UserPostListView.as_view(), name='user_posts'),
    #name='blog_home' is used in html for the href='{% url 'blog_home' %}' ; PostListView is a class based view
   
    path('post/<int:pk>/', PostDetailView.as_view(), name='post_detail'),
    #pk is the primary key. #class base view will look <app>/<model>_<viewtype>.html, which is blog-detail.html here
   
    path('post/new/', PostCreateView.as_view(), name='post_create'),
    #CreateView expect the html name to be post_form.html
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post_update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post_delete'), #DeleteView is expeting a html form called post_confirm_delete.html
    path('about', views.about, name='blog_about'),	   
]