from django.db import models

# Create your models here.
from django.db import models
from django.core.validators import MinValueValidator
from django.urls import reverse

def fotky(instance, filename):
    return "cats/" + str(instance.id) + "/fotka/" + filename

class Species(models.Model):
    jmeno_druhu = models.CharField(max_length=50, unique=True, verbose_name="Druh kočky",
                            help_text='Zadejte prosím druh kočky, popřípadě OwO pokud není známo')
    class Meta:
        ordering = ["jmeno_druhu"]
    def __str__(self):
        return self.jmeno_druhu

class Photo(models.Model):
    fotka = models.ImageField(upload_to='cats/fotky', blank=True, null=True, verbose_name="Fotka")
    nazev_fotky = models.CharField(max_length=50, blank=True, null=True, verbose_name="Název fotky")
    popisek_fotky = models.CharField(max_length=500, blank=True, null=True, verbose_name="popisek fotky")

    #druh = models.ForeignKey(Description_of_the_cat, on_delete=models.CASCADE)

    class Meta:
        ordering = ["fotka"]

    def __str__(self):
        return f"{self.fotka}"


    @property
    def filesize(self):
        x = self.fotka.size
        y = 512000
        if x < y * 1000:
            value = round(x/1024, 2)
            ext = ' KB'
        elif x < y * 1000**2:
            value = round(x/1024*2, 2)
            ext = ' MB'
        else:
            value = round(x/1024**3, 2)
            ext = ' GB'

        return str(value)+ext

class Description_of_the_cat(models.Model):
    jmeno = models.CharField(max_length=50, verbose_name="Jméno", blank=True)
    vek = models.IntegerField(verbose_name="Roky Kočky", blank=True, validators=[MinValueValidator(0.0)])
    vaha = models.IntegerField(verbose_name="Váha", blank=True, validators=[MinValueValidator(0.0)])
    popisek = models.CharField(max_length=500, verbose_name="popisek", blank=True)
    druh = models.ForeignKey(Species, on_delete=models.CASCADE)
    foto = models.ForeignKey(Photo, on_delete=models.CASCADE)

    #fotka = models.ImageField(upload_to='cats/fotky/%Y/%m/%d/', blank=True, null=True, verbose_name="Fotka")
    #species = models.ManyToManyField(Species, help_text='Vyberte fotku kočky')
    #fotky = models.ManyToManyField(Photo, help_text='Vyberte fotku kočky')
    class Meta:
        ordering = ["jmeno"]
    def __str__(self):
        return f"{self.jmeno}"

    def get_absolute_url(self):
        """Metoda vrací URL stránky, na které se vypisují podrobné informace o filmu"""
        return reverse('kocka_detail', args=[str(self.id)])


