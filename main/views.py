from django.shortcuts import render, HttpResponse

# Create your views here.

def homepage(request):
    return HttpResponse('hello Kairat')

def test(request):
    return render(request, 'test.html')

def third(request):
    return render(request, 'third.html')