from django.shortcuts import render, HttpResponse, redirect
from .models import ToDo, Book
# Create your views here.

def homepage(request):
    return render(request, 'index.html')

def test(request):
    todo_list = ToDo.objects.all()
    return render(request, 'test.html', {"todo_list":todo_list})

def third(request):
    return render(request, 'third.html')

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