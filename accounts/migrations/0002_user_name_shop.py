# Generated by Django 5.1.2 on 2024-10-12 05:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='name_shop',
            field=models.TextField(blank=True, null=True),
        ),
    ]