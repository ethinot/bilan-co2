from django.test import TestCase, RequestFactory
from .models import User_data, Consommation
from django.contrib.auth.models import User
from datetime import date
from .views import *

class UserTestCase(TestCase):

    def test_user_creation(self):
        user = User.objects.create_user(username='test_user', password='test_password')
        self.assertEqual(user.username, 'test_user')

class UserDataTestCase(TestCase):
    def setUp(self) -> None:
        self.user = User.objects.create_user(username='test_user', password='test_password')

    def test_user_data_creation(self):
        user_data = User_data.objects.get(user=self.user)
        self.assertEqual(user_data.user.username, 'test_user')
        self.assertEqual(str(user_data),'test_user')
        user_data.age = 25
        user_data.localisation = 'Paris'
        user_data.profession = 'ET'
        user_data.save()

        # Now retrieve the object again from the database to ensure changes are saved
        updated_user_data = User_data.objects.get(user=self.user)
        
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
        self.assertEqual(str(self.consommation),'Test Product')
        self.assertEqual(self.consommation.frequence_utilisation, 'JOURNALIER')
        self.assertEqual(self.consommation.quantite_co2, 10.0)
        self.assertEqual(self.consommation.type_consommation, 'FOSSILE')

        self.consommation.clean()
        
        self.consommation = Consommation.objects.create(user=self.user, nom_produit='Test Product', quantite_co2=10.0, type_consommation='FOSSILE')

        with self.assertRaises(ValidationError):
            self.consommation.clean()
        
        with self.assertRaises(ValidationError):
            self.consommation.date_consommation="LUNDI"
            self.consommation.frequence_utilisation='JOURNALIER'
            self.consommation.clean()
