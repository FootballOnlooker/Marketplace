from django.shortcuts import render


def index(request):
    return render(request, 'cores/index.html')


def contact(request):
    return render(request, 'cores/contact.html')


def about(request):
    return render(request, 'cores/about.html')
