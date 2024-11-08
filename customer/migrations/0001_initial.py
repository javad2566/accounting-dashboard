# Generated by Django 5.1.2 on 2024-10-13 05:20

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullname', models.CharField(blank=True, max_length=200, null=True, verbose_name='نام و نام خانوادگی')),
                ('phone', models.CharField(max_length=12, verbose_name='شماره تماس')),
                ('is_active', models.BooleanField(default=True, verbose_name='فعال')),
                ('is_paid', models.BooleanField(default=False, verbose_name='پرداخت شده ')),
                ('price', models.BigIntegerField(default=0, verbose_name='حساب در فروشگاه')),
                ('price_paid_all', models.BigIntegerField(default=0, verbose_name=' پول  پرداختی  ای کل    ')),
                ('price_mandeh', models.BigIntegerField(default=0, verbose_name='باقی مانده در فروشگاه')),
                ('discription', models.TextField(blank=True, max_length=300, null=True, verbose_name='توضیحات مدیر')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='تاریخ  ')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='تاریخ اضافه شدن')),
                ('image', models.ImageField(blank=True, null=True, upload_to='customer/', verbose_name='عکس پروفایل')),
                ('address', models.TextField(blank=True, null=True, verbose_name='ادرس کاربر')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'مشتری',
                'verbose_name_plural': 'مشتری ها  ',
            },
        ),
        migrations.CreateModel(
            name='Payments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('discription', models.TextField(blank=True, max_length=300, null=True, verbose_name='توضیحات مدیر')),
                ('price_paid', models.BigIntegerField(default=0, verbose_name=' پول  پرداختی لحظه ای   ')),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True, verbose_name='تاریخ اضافه شدن')),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='customer.customer')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'پرداخت  ',
                'verbose_name_plural': 'لیست پرداخت ها ',
            },
        ),
    ]
