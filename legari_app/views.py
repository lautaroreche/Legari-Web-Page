from django.shortcuts import render


def home(request):
    context = {}
    return render(request, 'index.html', context)


def artist(request):
    context = {}
    return render(request, 'artist.html', context)


def work(request, art_type):
    context = {}
    if art_type in ['obras-hierro', 'obras-piedra-madera', 'obras-madera-hierro']:
        return render(request, 'work.html', context)
    return render(request, 'index.html', context)

    
