from django.test import TestCase

class SimpleTestCase(TestCase):
    def test_numbers_equal(self):
        self.assertEqual(1, 2)