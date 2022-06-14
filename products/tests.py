from django.urls                import reverse
from django.contrib.auth.models import User

from rest_framework.test             import APITestCase
from rest_framework_simplejwt.tokens import RefreshToken

from products.models import Category, Product, Feeling, SkinType, Ingredient, Review


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


class ReviewTestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='example', password='Password123!')
        refresh   = RefreshToken.for_user(self.user)
        self.client.credentials(HTTP_AUTHORIZATION='Bearer {0}'.format(refresh.access_token))

        self.user_two = User.objects.create_user(username='example2', password='Password123!')
        refresh_two   = RefreshToken.for_user(self.user_two)
        self.client.credentials(HTTP_AUTHORIZATION='Bearer {0}'.format(refresh_two.access_token))

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
        
        self.review = Review.objects.create(
                                user    = self.user,
                                product = self.product,
                                content = 'test content'
                            )

    def test_reveiw_list_get(self):
        response = self.client.get(reverse('review-list', args=(self.product.id, )))
        self.assertEqual(response.status_code, 200)

    def test_review_detail_get(self):
        response = self.client.get(reverse('review-detail', args=(self.review.id, )))
        self.assertEqual(response.status_code, 200)
    
    def test_review_create(self):
        data = {
            "user"   : self.user_two,
            "product": self.product,
            "content": "test content"
        }
        response = self.client.post(reverse('review-create', args=(self.product.id, )), data)
        self.assertEqual(response.status_code, 201)