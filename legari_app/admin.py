from django.contrib import admin
from .models import Art
from django.contrib.sessions.models import Session


class ArtAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'summary', 'size', 'materials', 'art_type', 'starred')
    search_fields = ('id', 'title', 'summary', 'size', 'materials', 'art_type', 'starred')
    list_filter = ['art_type', 'starred']


admin.site.register(Session)
admin.site.register(Art, ArtAdmin)
