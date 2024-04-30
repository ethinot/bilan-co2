from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from geopy.geocoders import Nominatim
from django.core.exceptions import ValidationError
import pandas as pd
import unicodedata


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
        # TODO : probleme à regler 
        ##if self.localisation:
        ##    # Utilisation de Nominatim pour géocoder la localisation en France
        ##    geolocator = Nominatim(user_agent="geoapiExercises")
        ##    location = geolocator.geocode(self.localisation, country_codes='FR')

        ##    if location:
        ##        self.localisation = location.address
        ##    else:
        ##        raise ValueError("Localisation non valide ou non trouvée")

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

    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
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
    
class BD:
    def __init__(self,file:str) -> None:
        self.df =  pd.read_csv(file)
        self.name = file[:-4]
    def calcul(self,choix:str,quantite:float)->float:
        for i in range(len(self.df)-1):
            if  self.df.iloc[i].iloc[0]== choix:
                return self.df.iloc[i].iloc[1]*quantite
        raise ValueError("{self.name} non valide")
    def list_value(self)->list[str]:
        return list(self.df.iloc[:,0])
    def recherche(self,choix:str) -> list[str]:
        return [i for i in self.list_value() if choix.lower() in i.lower()]
    
class Alimentation(BD):
    filtre = pd.DataFrame()
    def list_value(self)->list[str]:
        return list(self.df.iloc[:,2])
    def list_categorie(self) -> dict[str]:
        res = {}
        for i in range(len(self.df.iloc[:,0])):
            if res.get(self.df.iloc[i,0]):
                res[self.df.iloc[i,0]].add(self.df.iloc[i,1])
            else:
                res[self.df.iloc[i,0]]={self.df.iloc[i,1]}
        return {k : list(v) for k,v in res.items()}
    def select_categorie(self,categorie : str) -> list[str]:
        l = [self.df.iloc[i,:] for i in range(len(self.df)) if self.df.iloc[i,0]==categorie]
        if l == []:
            raise ValueError("categorie non valide")
        else:
            self.filtre = pd.DataFrame(l)
        return list(set(self.filtre.iloc[:,1]))
    def select_sous_categorie(self,categorie: str)->list[str]:
        l = [self.filtre.iloc[i,:] for i in range(len(self.filtre)) if self.filtre.iloc[i,1]==categorie]
        if l == []:
            raise ValueError("sous categorie non valide")
        else:
            self.filtre = pd.DataFrame(l)
        return list(self.filtre.iloc[:,2])
    def calcul(self,choix:str,quantite:float)->float:
        if self.filtre.empty:
            f = self.df
        else:
            f = self.filtre      
        for i in range(len(f)):
            if f.iloc[i].iloc[2] == choix:
                return float(f.iloc[i].iloc[3])*quantite
        raise ValueError("produit non valide")
