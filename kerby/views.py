import random
from django.http import HttpResponse

def lotto_numbers(request):
    lotto_list = []
    for i in range(1, 6):
        lotto_list.append(random.sample(45, 6))
        html = "<html/> No.{} : %s <html/>".format(i) % lotto_list
    return HttpResponse(html)
