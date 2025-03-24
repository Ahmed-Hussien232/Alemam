# Generated by Django 5.1.7 on 2025-03-24 17:26

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Come_in',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cash_in', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=10, null=True)),
                ('notes', models.TextField(blank=True, null=True)),
                ('created_at3', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='Login',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=50)),
                ('password', models.CharField(max_length=50)),
                ('password2', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Payments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cash_out', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=10, null=True)),
                ('notes', models.TextField(blank=True, null=True)),
                ('created_at2', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='PrintOrder',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('printing_type', models.CharField(choices=[('color', 'ألوان'), ('black', 'أبيض وأسود')], max_length=10, verbose_name='نوع الطباعة')),
                ('paper_size', models.CharField(choices=[('A4', 'A4'), ('A3', 'A3')], max_length=10, verbose_name='حجم الورق')),
                ('paper_number', models.PositiveIntegerField(verbose_name='عدد الورق')),
                ('copy_number', models.PositiveIntegerField(verbose_name='عدد النسخ')),
                ('paper_price', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='سعر الورقة')),
                ('other', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='مبالغ إضافية')),
                ('pay', models.CharField(choices=[('cash', 'كاش'), ('vod-cash', 'محفظة إلكترونية')], max_length=10, verbose_name='طريقة الدفع')),
                ('total_price', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='الإجمالي')),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
    ]
