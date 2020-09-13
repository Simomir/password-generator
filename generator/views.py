import random
import string
from django.shortcuts import render


def home(request):
    return render(request, 'generator/home.html')


def password(request):
    result = ''

    pool = list(string.ascii_lowercase)
    length = int(request.GET.get('length', 12))

    if request.GET.get('uppercase'):
        pool.extend(string.ascii_uppercase)

    if request.GET.get('numbers'):
        pool.extend(string.digits)

    if request.GET.get('special'):
        pool.extend(string.punctuation)

    for x in range(length):
        result += random.choice(pool)

    return render(request, 'generator/password.html', {'password': result})


def about(request):
    return render(request, 'generator/about.html')
