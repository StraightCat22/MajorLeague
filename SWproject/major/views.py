from django.shortcuts import render


def index(request): #만들어야함
    return render(request, 'index.html')


def dashboard(request):
    return render(request, 'major/dashboard.html')


def user(request):
    return render(request, 'major/user.html')


def score(request):
    return render(request, 'major/score.html')