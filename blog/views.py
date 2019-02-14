import random
from django.shortcuts import render
from django.http import HttpResponse

def articles_by_year(request, year):
    return HttpResponse(f'''
        {year}년도에 대한 목록
    ''')

def index(request):
    return render(request, 'blog/index.html')

def hello_times(request, times):
    message = "안녕하세요 " * times
    return HttpResponse(message)

def lotto_numbers(request, numbers):
    lotto_list = []
    for i in range(1, 6):
        lotto_list.append(random.sample(45, 6))
        message = "<html>Suggestion No.{} : </html>".format(i)
        return HttpResponse(message)

