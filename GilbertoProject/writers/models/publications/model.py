from django.db import models
from django.urls import reverse
from django.core.validators import MaxValueValidator
from ..writers.model import Writers


class Publications (models.Model):
    website = models.TextChoices('Business2Community', 'De Finanzas', 'ComprarAcciones')
    category = models.TextChoices('Gambling', 'Criptomonedas', 'Marketing', 'Acciones')
    publication_date = models.DateField(default="YYYY-MM-DD", null= False, blank= False)
    title = models.CharField(max_length=20000)
    url = models.URLField(unique=False)
    words = models.IntegerField(validators=[MaxValueValidator(7000)], help_text='# de palabras')
    COUNTRY_CHOICE=(
        ('Perú', 'Perú'),
        ('Colombia','Colombia'),
        ('Argentina','Argentina'),
        ('España', 'España'),
        ('Chile', 'Chile'),
        ('México', 'México'),
        ('EEUU español', 'EEUU español')
    )
    country = models.Choices(COUNTRY_CHOICE)
    author = models.ForeignKey(Writers.first_name, Writers.last_name, on_delete=models.CASCADE)
    obs = models.CharField(max_length=50000)

    class Meta:
            verbose_name = ("Registro de publicaciones")
            verbose_name_plural = ("Registro de publicaciones")
    
    def get_absolute_url(self):
            return reverse("publication_detail", args=[str(self.id)])
