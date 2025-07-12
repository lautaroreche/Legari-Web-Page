from django.db import models
from django.utils.translation import gettext_lazy as _
from cloudinary.models import CloudinaryField


class Art(models.Model):
    TYPE_CHOICES = [
        ('obras-hierro', 'Obras Hierro'),
        ('obras-piedra-madera', 'Obras Piedra & Madera'),
        ('obras-madera-hierro', 'Obras Madera & Hierro'),
    ]

    id = models.AutoField(primary_key=True)
    title = models.CharField(_("Nombre"), max_length=150)
    summary = models.CharField(_("Descripción"), max_length=400)
    size = models.CharField(_("Tamaño"), max_length=50)
    materials = models.CharField(_("Materiales"), max_length=150)
    art_type = models.CharField(_("Tipo"), max_length=50, choices=TYPE_CHOICES, default='obras-hierro')
    starred = models.BooleanField(_("Destacada"), default=False)
    image = CloudinaryField(_("Imagen"), resource_type='image')
    
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name="Obra de arte"
        verbose_name_plural="Obras de arte"
