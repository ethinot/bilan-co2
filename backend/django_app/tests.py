from django.test import TestCase
from django_app.models import BD, Alimentation
# Create your tests here.

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