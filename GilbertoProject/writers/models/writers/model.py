from django.db import models
from django.urls import reverse

class Writers (models.Model):
    first_name = models.CharField(max_length=30, help_text='Nombre')
    last_name = models.CharField(max_length=50, help_text='Apellido')
    initial_date = models.DateField(default="YYYY-MM-DD", null= True, blank= True)
    price_per_word = models.DecimalField(max_digits=5, decimal_places=4)
    GEO_CHOICE = (
        ('Europa', 'Europa'),
        ('África', 'África'),
        ('Norteamérica', 'Norteamérica'),
        ('Suramérica', 'Suramérica'),
        ('Centroamérica', 'Centroamérica'),
        ('Asia', 'Asia'),
        ('Oceanía', 'Oceanía')
    )
    geo = models.Choices(GEO_CHOICE)
    finish_date = models.DateField(default='YYYY-MM-DD', null=True, blank=True)

    def __str__(self):
            return self.first_name +" "+ self.last_name
    
    class Meta:
            verbose_name = ("Formulario de registro de redactores")
            verbose_name_plural = ("Formulario de registro de redactores")
    
    def get_absolute_url(self):
            return reverse("writer_detail", args=[str(self.id)])
