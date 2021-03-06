from django.shortcuts import render, HttpResponse, redirect
from .models import ToDo, Book
# Create your views here.

def homepage(request):
    return render(request, 'index.html')

def test(request):
    todo_list = ToDo.objects.all()
    return render(request, 'test.html', {"todo_list":todo_list})

def book(request):
    return render(request, 'book.html')

def get_books(request):
    book_list = Book.objects.all()
    return render(request, 'books.html', {"book_list":book_list})

def add_todo(request):
    form = request.POST
    text = form["todo_text"]
    todo = ToDo(text=text)
    todo.save()
    return redirect(test)

def delete_todo(request, id):
    todo = ToDo.objects.get(id=id)
    todo.delete()
    return redirect(test)

def favorite_todo(request, id):
    todo = ToDo.objects.get(id=id)
    todo.is_favorite = True
    todo.save()
    return redirect(test)

def unfavorite_todo(request, id):
    todo = ToDo.objects.get(id=id)
    todo.is_favorite = False
    todo.save()
    return redirect(test)

def todo_complete(request, id):
    todo = ToDo.objects.get(id=id)
    todo.is_closed = not todo.is_closed 
    todo.save()
    return redirect(test)

def book_favorite(request, id):
    book = Book.objects.get(id=id)
    book.is_favorites = True
    book.save()
    return redirect(get_books)

def book_unfavorite(request, id):
    book = Book.objects.get(id=id)
    book.is_favorites = False
    book.save()
    return redirect(get_books)

def book_remove(request, id):
    book = Book.objects.get(id=id)
    book.delete()
    return redirect(get_books)

def books_detail(request, id):
    item = Book.objects.get(id=id)
    return render(request, 'books_detail.html', {"book":item})
    