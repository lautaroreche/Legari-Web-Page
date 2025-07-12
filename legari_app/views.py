from django.shortcuts import render


def home(request):
    context = {}
    return render(request, 'index.html', context)


def artist(request):
    context = {}
    return render(request, 'artist.html', context)


def work(request):
    context = {}
    return render(request, 'work.html', context)
