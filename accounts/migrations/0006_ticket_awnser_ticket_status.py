# Generated by Django 5.1.2 on 2024-10-31 05:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_alter_alert_customer_alter_alert_product'),
    ]

    operations = [
        migrations.AddField(
            model_name='ticket',
            name='awnser',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='ticket',
            name='status',
            field=models.BooleanField(default=False),
        ),
    ]
