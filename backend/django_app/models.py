from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class User_data(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)

    champ_1=models.CharField(max_length=255, null=True, blank=True)
    champ_2=models.CharField(max_length=255, null=True, blank=True)
    champ_3=models.CharField(max_length=255, null=True, blank=True)
    champ_4=models.CharField(max_length=255, null=True, blank=True)
    champ_5=models.CharField(max_length=255, null=True, blank=True)

    # TODO : rajouter les champs necessaires pour le projet

    def __str__(self):
        return str(self.user.username)   

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        User_data.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.user_data.save()