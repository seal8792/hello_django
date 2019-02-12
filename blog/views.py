from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request, 'blog/index.html')

def hello_times(request, times) :
    message = "안녕하세요" * times
    return HttpResponse(message)

