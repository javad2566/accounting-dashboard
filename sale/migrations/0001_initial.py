# Generated by Django 5.1.2 on 2024-10-27 13:38

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('customer', '0002_alter_customer_options'),
        ('product', '0004_alter_product_category'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductItemSale',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price_selling', models.BigIntegerField(blank=True, default=0, null=True, verbose_name='قیمت فروش')),
                ('tedad', models.PositiveBigIntegerField(default=0, verbose_name='موجودی')),
                ('price_kol', models.BigIntegerField(blank=True, default=0, null=True)),
                ('created_at', models.DateField(auto_now_add=True, null=True, verbose_name='تاریخ افزودن محصول')),
                ('product', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='product.product')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'ایتم محصول',
                'verbose_name_plural': 'ایتم محصولات برای فروش',
            },
        ),
        migrations.CreateModel(
            name='InvoiceSale',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateField(auto_now_add=True, null=True, verbose_name='تاریخ افزودن محصول')),
                ('off', models.IntegerField(blank=True, default=0, null=True, verbose_name='تخفیف  شرکت ')),
                ('price_nahayi', models.BigIntegerField(blank=True, default=0, null=True)),
                ('last_price', models.BigIntegerField(blank=True, default=0, null=True)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='customer.customer')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('product', models.ManyToManyField(blank=True, to='sale.productitemsale')),
            ],
            options={
                'verbose_name': 'فروش  محصول',
                'verbose_name_plural': 'فروش  محصولات  ',
            },
        ),
    ]