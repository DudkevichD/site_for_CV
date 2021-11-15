from django.urls import path
from .views import HomeView, PostByCategory, Search, GetOnePost, PostByTag, register, user_login, user_logout, feedback

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('category/<str:slug>/', PostByCategory.as_view(), name='category'),
    path('post/<str:slug>/', GetOnePost.as_view(), name='post'),
    path('tag/<str:slug>/', PostByTag.as_view(), name='tag'),
    path('search/', Search.as_view(), name='search'),
    path('register/', register, name='register'),
    path('login/', user_login, name='login'),
    path('logout/', user_logout, name='exit'),
    path('feedback/', feedback, name='feedback'),
    ]
