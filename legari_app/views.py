from django.shortcuts import render


def home(request):
    context = {}
    return render(request, 'index.html', context)


def artist(request):
    context = {}
    return render(request, 'artist.html', context)


def work(request, art_type):
    context = {}
    art = {
        'obras-hierro': 'Obras Hierro',
        'obras-piedra-madera': 'Obras Piedra & Madera',
        'obras-madera-hierro': 'Obras Madera & Hierro',
    }
    if art_type in art:
        context['art_type'] = art_type
        context['title'] = art[art_type]
        return render(request, 'arts.html', context)
    return render(request, 'index.html', context)

    
