# Generated by Django 4.0.3 on 2022-06-02 16:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0008_remove_product_user'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='feelings',
            new_name='feeling',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='skin_types',
            new_name='skin_type',
        ),
        migrations.AddField(
            model_name='product',
            name='ingredient',
            field=models.ManyToManyField(through='products.ProductIngredient', to='products.ingredient'),
        ),
    ]