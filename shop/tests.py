from django.test import TestCase
from django.urls import reverse

class ShopViewTests(TestCase):
    def test_product_list_status_code(self):
        response = self.client.get(reverse('shop:product_list'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'shop/product_list.html')
        self.assertTemplateUsed(response, 'base.html')
        self.assertContains(response, 'My first Product List')
