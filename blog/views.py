import random
import requests
from bs4 import BeautifulSoup
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

def naver_realtime_keywords(request):
    res = requests.get("http://naver.com")
    html = res.text
    soup = BeautifulSoup(html, 'html.parser')
    tag_list = soup.select('.PM_CL_realtimeKeyword_rolling .ah_k')
    text = '<br/>\n'.join([tag.text for tag in tag_list])
    return HttpResponse(text)

def lotto_numbers(request):
    html_list = []
    for i in range(1, 6):
        lotto_list = random.sample(range(1, 46), 6)
        lotto_list.sort()
        html = "<html><body>No.{} : %s </body></html>".format(i) % lotto_list
        html_list.append(html)
    return HttpResponse(html_list)
