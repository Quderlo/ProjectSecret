from django.shortcuts import render


def homepage_view(request):
    return render(request, 'main.html')

def index_view(request):
    return render(request, 'index.html')