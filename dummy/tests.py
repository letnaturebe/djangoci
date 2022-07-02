from django.test import TestCase

from dummy.models import Ci


class CiTest(TestCase):
    def test_plus(self):
        self.assertEqual(1+1, 2)

    def test_minus(self):
        self.assertEqual(1-1, 0)

    def test_model(self):
        name = "leemoney93"
        age = 100
        ci = Ci.objects.create(name=name, age=age)
        self.assertEqual(ci.name, name)
        self.assertEqual(ci.age, age)