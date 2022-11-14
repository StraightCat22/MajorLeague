from django.shortcuts import render


def index(request): #만들어야함
    return render(request, 'index.html')


def dashboard(request):
    return render(request, 'major/dashboard.html')