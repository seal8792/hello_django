from django.shortcuts import render
from django.http import HttpResponse
import random

def lotto_numbers(request, times) :
    lotto_list = []
    for i in range(1,6) :
        lotto_list.append(random.sample(45,6))
        html = "<html/> No.{} : %s <html/>".format(i) % lotto_list
    return HttpResponse(html)
