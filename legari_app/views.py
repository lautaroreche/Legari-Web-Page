from django.shortcuts import render
from legari_app.models import Art
import json
from itertools import zip_longest


ART_TYPE_MAP = dict(Art.TYPE_CHOICES)


def mech_arts(arts):
    meched_arts = []
    grouped = {key: [] for key in ART_TYPE_MAP.keys()}
    for art_object in arts:
        if art_object.art_type in grouped:
            grouped[art_object.art_type].append(art_object)
    grouped_lists = list(grouped.values())
    for group in zip_longest(*grouped_lists):
        for art_object in group:
            if art_object is not None:
                meched_arts.append(art_object)
    return meched_arts


def home(request):
    context = {}
    arts = Art.objects.filter(starred=True)
    ordered_arts = mech_arts(arts)
    context['arts'] = ordered_arts
    return render(request, 'index.html', context)


def artist(request):
    context = {}
    return render(request, 'artist.html', context)


def work(request, art_type=None):
    context = {}
    if art_type is None:
        arts = Art.objects.all()
    else:
        arts = Art.objects.filter(art_type=art_type)
        if art_type in ART_TYPE_MAP:
            context['title'] = ART_TYPE_MAP[art_type]
            context['art_type'] = art_type
    ordered_arts = mech_arts(arts)
    context['arts'] = ordered_arts
    return render(request, 'arts.html', context)


def art(request, art_id):
    context = {}
    art_object = Art.objects.get(id=art_id)

    image_urls = [art_object.image1.url]
    for image_field in ['image2', 'image3', 'image4', 'image5']:
        image = getattr(art_object, image_field)
        if image:
            image_urls.append(image.url)

    context['art'] = art_object
    context['art_images_json'] = json.dumps(image_urls)
    return render(request, 'art.html', context)
