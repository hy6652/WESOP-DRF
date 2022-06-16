from django.urls                import reverse
from django.contrib.auth.models import User

from rest_framework.test             import APITestCase
from rest_framework_simplejwt.tokens import RefreshToken

from carts.models    import Cart
from products.models import Category, Product, Feeling, SkinType, Ingredient


class CartTest(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='example', password='Password123!')
        refresh   = RefreshToken.for_user(self.user)
        self.client.credentials(HTTP_AUTHORIZATION='Bearer {0}'.format(refresh.access_token))
        
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

        self.cart = Cart.objects.create(
                                user     = self.user,
                                product  = self.product,
                                quantity = 3
                            )

    def test_cart_list_get(self):
        response = self.client.get(reverse('cart-list'))
        self.assertEqual(response.status_code, 200)
    
    def test_cart_detail_get(self):
        response = self.client.get(reverse('cart-detail', args=(self.cart.id, )))
        self.assertEqual(response.status_code, 200)
    
    def test_cart_create(self):
        data = {
            "product" : self.product.id,
            "quantity": 5
        }
        response = self.client.post(reverse('cart-list'), data)
        self.assertEqual(response.status_code, 201)
    
    def test_cart_update(self):
        data = {
            "product" : self.product.id,
            "quantity": 3
        }
        response = self.client.put(reverse('cart-detail', args=(self.cart.id, )), data)
        self.assertEqual(response.status_code, 200)
    
    def test_cart_delete(self):
        response = self.client.delete(reverse('cart-detail', args=(self.cart.id, )))
        self.assertEqual(response.status_code, 204)