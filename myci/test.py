from django.test import TestCase


class CiTest(TestCase):
    def test_plus(self):
        self.assertEqual(1+1, 2)

    def test_minus(self):
        self.assertEqual(1-1, 0)
