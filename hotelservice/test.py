# tests/test_utils.py

from django.test import TestCase


class TestUtils(TestCase):
    def test_product_str(self):
        # Test the __str__ method of the Product model
        self.assertEqual(str(self.product1), 'Product 1')
        self.assertEqual(str(self.product2), 'Product 2')

    def test_product_attributes(self):
        # Test attributes of Product objects
        self.assertEqual(self.product1.name, 'Contact1 1')
        self.assertEqual(self.product1.price, 10.99)
        self.assertEqual(self.product1.description, 'Description for Product 1')

        self.assertEqual(self.product2.name, 'Product 2')
        self.assertEqual(self.product2.price, 5.99)
        self.assertEqual(self.product2.description, 'Description for Product 2')
    def test_calculate_total_price(self):        
        total_price = 24.97
        self.assertAlmostEqual(total_price, 24.97, places=2)
