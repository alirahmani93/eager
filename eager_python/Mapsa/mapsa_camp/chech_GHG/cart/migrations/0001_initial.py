# Generated by Django 3.2.7 on 2021-09-14 07:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('users', '0010_auto_20210913_2016'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cart_uuid', models.UUIDField(default=None, unique_for_date=1, verbose_name='شماره کارت ساخته شده')),
                ('cart_status', models.CharField(choices=[('on_cart', 'on_cart'), ('ready_to_pay', 'ready_to_pay')], default=('on_cart', 'on_cart'), max_length=100)),
                ('active', models.BooleanField(default=True)),
                ('user_fk', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='users.regular')),
            ],
        ),
        migrations.CreateModel(
            name='CartItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('quantity', models.IntegerField(default=0)),
                ('active', models.BooleanField(default=True)),
                ('cart_fk', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.RESTRICT, to='cart.cart')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
