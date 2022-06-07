from django.db                  import models
from django.contrib.auth.models import User

from products.models import Product
from cores.timestamp import TimeStamp


class Cart(TimeStamp):
    user     = models.ForeignKey(User, on_delete=models.CASCADE)
    product  = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)

    class Meta:
        db_table = 'carts'