# Generated by Django 5.1.2 on 2024-11-03 05:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shopping', '0006_invoiceshop_phone_company'),
    ]

    operations = [
        migrations.AlterField(
            model_name='invoiceshop',
            name='keriyeh',
            field=models.PositiveBigIntegerField(blank=True, default=0, null=True, verbose_name='تخفیف  شرکت '),
        ),
        migrations.AlterField(
            model_name='invoiceshop',
            name='last_price',
            field=models.PositiveBigIntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='invoiceshop',
            name='off',
            field=models.PositiveBigIntegerField(blank=True, default=0, null=True, verbose_name='تخفیف  شرکت '),
        ),
        migrations.AlterField(
            model_name='invoiceshop',
            name='price_nahayi',
            field=models.PositiveBigIntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='productitem',
            name='price',
            field=models.PositiveBigIntegerField(blank=True, default=0, null=True, verbose_name='قیمت خرید'),
        ),
        migrations.AlterField(
            model_name='productitem',
            name='price_kol',
            field=models.PositiveBigIntegerField(blank=True, default=0, null=True),
        ),
    ]
