"""todo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from main.views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', homepage, name='home'),
    path('test/', test, name='test'),
    path('test3/', third, name='third'),
    path('book/', book, name='book'),
    path("add-todo/", add_todo, name='add-todo'),
    path('books/', get_books, name='get_books'),
    path('delete-todo/<id>/', delete_todo, name='delete-todo'),
    path('favorite-todo/<id>/', favorite_todo, name='favorite-todo'),
    path('unfavorite-todo/<id>/', unfavorite_todo, name='unfavorite-todo'),
    path('todo-complete/<id>/', todo_complete, name='todo-complete'),
    path('book-favorite/<id>/', book_favorite, name='book-favorite'),
    path('book-unfavorite/<id>/', book_unfavorite, name='book-unfavorite'),
    path('book-remove/<id>/', book_remove, name='book-remove'),

] + static(settings.STATIC_URL, documet_root=settings.STATIC_ROOT)\
  + static(settings.MEDIA_URL, documet_root=settings.MEDIA_ROOT)
