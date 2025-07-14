from django.shortcuts import render
from legari_app.models import Art
import json


def home(request):
    context = {}
    arts = Art.objects.filter(starred=True)
    context['arts'] = arts
    return render(request, 'index.html', context)


def artist(request):
    context = {}
    return render(request, 'artist.html', context)


def work(request, art_type):
    context = {}
    arts = Art.objects.filter(art_type=art_type)
    
    art_type_map = {
        'obras-hierro': 'Obras Hierro',
        'obras-piedra-madera': 'Obras Piedra & Madera',
        'obras-madera-hierro': 'Obras Madera & Hierro',
    }
    if art_type in art_type_map:
        context['art_type'] = art_type
        context['title'] = art_type_map[art_type]
        context['arts'] = arts
        return render(request, 'arts.html', context)
    return render(request, 'index.html', context)


def art(request, art_id):
    context = {}
    object_art = Art.objects.get(id=art_id)

    image_urls = [object_art.image1.url]
    for image_field in ['image2', 'image3', 'image4', 'image5']:
        image = getattr(object_art, image_field)
        if image:
            image_urls.append(image.url)

    context['art'] = object_art
    context['art_images_json'] = json.dumps(image_urls)
    return render(request, 'art.html', context)

