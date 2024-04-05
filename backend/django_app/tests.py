from django.test import TestCase
from django_app.models import Transport
# Create your tests here.

class TransportTestCase(TestCase):
    def setUp(self) -> None:
        self.test = Transport()
     
    def test_calcul(self):
        self.assertEqual(self.test.calcul("TER",100), 100*0.03)
    def test_calcul_gestion_erreur(self):
        with self.assertRaises(ValueError):
            self.test.calcul("fusée",300000)