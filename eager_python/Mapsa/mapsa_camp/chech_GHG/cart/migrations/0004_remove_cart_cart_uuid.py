# Generated by Django 3.2.7 on 2021-09-15 14:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0003_alter_cart_user_fk'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cart',
            name='cart_uuid',
        ),
    ]
