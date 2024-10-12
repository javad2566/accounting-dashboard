# Generated by Django 5.1.2 on 2024-10-12 05:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('fullname', models.CharField(blank=True, max_length=200, null=True, verbose_name='نام و نام خانوادگی')),
                ('phone', models.CharField(max_length=12, unique=True, verbose_name='شماره تماس')),
                ('is_active', models.BooleanField(default=True, verbose_name='فعال')),
                ('is_admin', models.BooleanField(default=False, verbose_name='ادمین')),
                ('email', models.EmailField(blank=True, max_length=254, null=True, verbose_name='ایمیل')),
                ('discription', models.TextField(blank=True, max_length=300, null=True, verbose_name='توضیحات کاربر')),
                ('created_at', models.DateTimeField(auto_now=True, verbose_name='تاریخ اضافه شدن')),
                ('image', models.ImageField(blank=True, null=True, upload_to='user_image', verbose_name='عکس پروفایل')),
                ('address', models.TextField(blank=True, null=True, verbose_name='ادرس کاربر')),
            ],
            options={
                'verbose_name': 'کاربر',
                'verbose_name_plural': 'کاربر ها ',
            },
        ),
        migrations.CreateModel(
            name='OTP',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone', models.CharField(blank=True, max_length=30, null=True)),
                ('code', models.BigIntegerField(default=1, null=True)),
                ('token', models.CharField(max_length=200, null=True, verbose_name='توکن کاربر')),
                ('password', models.CharField(max_length=200, null=True, verbose_name='رمز کاربر')),
                ('created_at', models.DateTimeField(auto_now=True, verbose_name='تاریخ اضافه شدن')),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'otp',
                'verbose_name_plural': 'opts',
            },
        ),
    ]