# Generated by Django 3.2.7 on 2021-09-15 15:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0005_auto_20210915_1232'),
        ('cart', '0006_alter_cart_user_fk'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cartitem',
            name='cart_fk',
        ),
        migrations.AddField(
            model_name='cart',
            name='cart_item',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.RESTRICT, to='cart.cartitem'),
        ),
        migrations.AlterField(
            model_name='cartitem',
            name='product_fk',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.RESTRICT, to='product.product'),
        ),
    ]
