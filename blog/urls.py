
from django.urls import path
from django.urls import register_converter
from blog.views import index, hello_times, articles_by_year, lotto_numbers
from blog.converters import FourDigitYearConverter

register_converter(FourDigitYearConverter, 'year')

app_name = 'blog'

urlpatterns = [
    path('articles/<year:year>/', articles_by_year),
    path('hello_times/<int:times>/', hello_times),
    path('articles/<year:year>', articles_by_year),
    path('lotto_numbers/', lotto_numbers),
    path('', index),
    ]
