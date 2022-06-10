from django.urls import reverse

from rest_framework.test import APITestCase

from products.models import Category, Product, Feeling, SkinType, Ingredient


class CategoryTestCase(APITestCase):
    def setUp(self):
        self.category = Category.objects.create(
                                    category_name    = 'test category',
                                    main_description = 'test main description',
                                    sub_description  = 'test sub description'
                                )

    def test_category_list_get(self):
        response = self.client.get(reverse('category-list'))
        self.assertEqual(response.status_code, 200)
    
    def test_category_detail_get(self):
        response = self.client.get(reverse('category-detail', args=(self.category.id, )))
        self.assertEqual(response.status_code, 200)


class ProductTestCase(APITestCase):
    def setUp(self):
        self.category = Category.objects.create(
                                    category_name    = 'test category',
                                    main_description = 'test main description',
                                    sub_description  = 'test sub description'
                                )

        self.feeling    = Feeling.objects.create(name='test feeling')
        self.skin_type  = SkinType.objects.create(name='test skin type')
        self.ingredient = Ingredient.objects.create(name='test ingredient')

        self.product = Product.objects.create(
            name        = 'test name',
            price       = 1000.00,
            size        = 'test size',
            description = 'test description',
            category    = self.category,
            howtouse    = {'test':'test'},
            badge       = 'test badge'
        )

    def test_product_list_get(self):
        response = self.client.get(reverse('product-list'))
        self.assertEqual(response.status_code, 200)
    
    def test_product_detail_get(self):
        response = self.client.get(reverse('product-detail', args=(self.product.id, )))
        self.assertEqual(response.status_code, 200)