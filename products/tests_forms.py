from django.test import TestCase
from .forms import ProductForm
import random

class TestItemForm(TestCase):
    def test_item_name_is_required(self):
        form = ProductForm({'name': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('name', form.errors.keys())
        self.assertEqual(form.errors['name'][0], 'This field is required.')


