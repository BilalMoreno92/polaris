# Generated by Django 5.0.3 on 2024-03-09 10:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('erp', '0005_category_employee_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='description',
            field=models.TextField(blank=True, max_length=500, null=True, verbose_name='Descripción'),
        ),
        migrations.AlterField(
            model_name='type',
            name='description',
            field=models.TextField(blank=True, max_length=500, null=True, verbose_name='Descripción'),
        ),
    ]
