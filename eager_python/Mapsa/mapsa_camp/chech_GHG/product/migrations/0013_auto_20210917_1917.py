# Generated by Django 3.2.7 on 2021-09-17 19:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0012_alter_product_upc'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attribute',
            name='attrs',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='attrval', to='product.attributekey'),
        ),
        migrations.AlterField(
            model_name='attribute',
            name='product',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='attrproduct', to='product.product'),
        ),
    ]
