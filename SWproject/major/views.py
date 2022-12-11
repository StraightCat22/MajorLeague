from django.shortcuts import render


def index(request): #만들어야함
    return render(request, 'major/index.html')


def dashboard(request):
    return render(request, 'major/dashboard.html')


def CSresult(request):
    return render(request, 'major/CSresult.html')

def CSinfo(request):
    return render(request, 'major/CSinfo.html')

def FNresult(request):
    return render(request, 'major/FNresult.html')

def user(request):
    return render(request, 'major/user.html')


def score(request):
    return render(request, 'major/score.html')


def register(request):
    return render(request, 'major/register.html')


def apply(request):
    return render(request, 'major/apply.html')