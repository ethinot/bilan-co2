from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from geopy.geocoders import Nominatim
from django.core.exceptions import ValidationError

class User_data(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    age = models.IntegerField(null=True)
    localisation = models.CharField(max_length=255, blank=True, null=True)
    profession_choices = [
        ('ET', 'Étudiant'),
        ('EMP', 'Employé'),
        ('CAD', 'Cadre'),
        ('CHOM', 'Chômeur'),
    ]
    profession = models.CharField(max_length=4, choices=profession_choices, blank=True)

    def save(self, *args, **kwargs):
        if self.localisation:
            # Utilisation de Nominatim pour géocoder la localisation en France
            geolocator = Nominatim(user_agent="geoapiExercises")
            location = geolocator.geocode(self.localisation, country_codes='FR')

            if location:
                self.localisation = location.address
            else:
                raise ValueError("Localisation non valide ou non trouvée")

        super(User_data, self).save(*args, **kwargs)

    def __str__(self):
        return str(self.user.username)   

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        User_data.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.user_data.save()


class Consommation(models.Model):
    # TODO lié la consommation aux données du csv

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    nom_produit = models.CharField(max_length=255) # TODO : nom du produit en type choice des donnéesCSV. Une idée crée un champ categorie pour facilité la selection
    FREQUENCE_CHOICES = [
        ('JOURNALIER', 'Journalier'),
        ('HEBDO', 'Hebdomadaire'),
        ('MENSUELLE', 'Mensuelle'),
    ]
    frequence_utilisation = models.CharField(max_length=20, choices=FREQUENCE_CHOICES, blank=True)
    quantite_co2 = models.FloatField()
    date_consommation = models.DateField(null=True, blank=True)
    TYPE_CHOICES = [
        ('FOSSILE', 'Fossile'),
        ('ALIMENTAIRE', 'Alimentaire'),
        ('TRANSPORT', 'Transport'),
    ]
    type_consommation = models.CharField(max_length=20, choices=TYPE_CHOICES)

    def clean(self):
        super().clean()
        if self.frequence_utilisation and self.date_consommation:
            raise ValidationError("Vous ne pouvez pas spécifier à la fois la fréquence d'utilisation et la date de consommation")
        if not self.frequence_utilisation and not self.date_consommation:
            raise ValidationError("La fréquence d'utilisation ou la date de consommation doit être spécifiée")
            
    def __str__(self):
        return str(self.nom_produit)  