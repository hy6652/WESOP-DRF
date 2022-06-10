from django.urls import reverse

from rest_framework.test import APITestCase

from products.models import Category


class CategoryTestCase(APITestCase):
    def setUp(self):
        self.category = Category.objects.create(
                                    category_name    = 'test category',
                                    main_description = 'test main description',
                                    sub_description  = 'test sub description'
                                )

    def test_category_list(self):
        response = self.client.get(reverse('category-list'))
        self.assertEqual(response.status_code, 200)
    
    def test_category_detail(self):
        response = self.client.get(reverse('category-detail', args=(self.category.id, )))
        self.assertEqual(response.status_code, 200)