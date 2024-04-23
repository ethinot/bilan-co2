from django.test import TestCase
from .models import User_data, Consommation
from django.core.exceptions import ValidationError 
from django.contrib.auth.models import User
from datetime import date

class UserTestCase(TestCase):

    def test_user_creation(self):
        user = User.objects.create_user(username='test_user', password='test_password')
        self.assertEqual(user.username, 'test_user')

class UserDataTestCase(TestCase):

    def test_user_data_creation(self):
        user = User.objects.create_user(username='test_user', password='test_password')
        user_data = User_data.objects.get(user=user)
        self.assertEqual(user_data.user.username, 'test_user')
        user_data.age = 25
        user_data.localisation = 'Paris'
        user_data.profession = 'ET'
        user_data.save()

        # Now retrieve the object again from the database to ensure changes are saved
        updated_user_data = User_data.objects.get(user=user)
        
        self.assertEqual(updated_user_data.age, 25)
        self.assertEqual(updated_user_data.localisation, 'Paris')
        self.assertEqual(updated_user_data.profession, 'ET')

class ConsommationModelTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='test_user', password='test_password')
        self.consommation = Consommation.objects.create(user=self.user, nom_produit='Test Product', frequence_utilisation='JOURNALIER', quantite_co2=10.0, type_consommation='FOSSILE')

    def test_consommation_creation(self):
        self.assertEqual(self.consommation.user.username, 'test_user')
        self.assertEqual(self.consommation.nom_produit, 'Test Product')
        self.assertEqual(self.consommation.frequence_utilisation, 'JOURNALIER')
        self.assertEqual(self.consommation.quantite_co2, 10.0)
        #self.assertEqual(self.consommation.type_consommation, 'FOSSILE')
