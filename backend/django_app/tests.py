from django.test import TestCase
from .models import User_data, Consommation, BD, Alimentation
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

class TransportTestCase(TestCase):
    def setUp(self) -> None:
        self.test = BD("transport.csv")
     
    def test_calcul(self):
        self.assertEqual(self.test.calcul("TER",100), 100*0.03)
    def test_calcul_gestion_erreur(self):
        with self.assertRaises(ValueError):
            self.test.calcul("fusée",300000)

class EnergieTestCase(TestCase):
    def setUp(self) -> None:
        self.test = BD("energie.csv")

    def test_calcul(self):
        self.assertEqual(self.test.calcul("Électricité(centrale nucléaire)",100),100*0.006)
    def test_calcul_gestion_erreur(self):
        with self.assertRaises(ValueError):
            self.test.calcul("tachyon",1000000)


class AlimentationTestCase(TestCase):
    def setUp(self) -> None:
        self.test = Alimentation("alimentation.csv")
    def test_calcul(self):
        self.assertEqual(self.test.calcul("Agar (algue), cru",100),100*0.0389)
    def test_calcul_gestion_erreur(self):
        with self.assertRaises(ValueError):
            self.test.calcul("Gloubi-boulga",1000000)
    def test_categorie(self):
        quantite = 10
        produit = "Eau minérale Rozana, embouteillée, gazeuse, fortement minéralisée (Beauregard, 63)"
        calcul_sans_selection =self.test.calcul(produit, quantite)
        self.test.select_categorie("boissons")
        self.test.select_sous_categorie("eaux")
        self.assertEqual(calcul_sans_selection,self.test.calcul(produit,quantite))

 
