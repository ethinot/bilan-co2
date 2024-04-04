from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.apps import apps



class User_data(models.Model):
    user_tag = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    
    champ_1 = models.CharField(null=True, blank=True)
    champ_2 = models.IntegerField(null=True, blank=True)
    # ... # TODO : modifier les champs en fonction de l'organisation
    champ_n = models.IntegerField(null=True, blank=True)

    class Meta:
        app_label = 'User_data'

    def __str__(self):
        return str(self.user.username)
    
#@receiver(post_save, sender=User)
#def create_user_profile(sender, instance, created, **kwargs):
#    if created:
#        User_data.objects.create(user=instance)