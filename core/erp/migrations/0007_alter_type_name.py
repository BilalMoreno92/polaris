# Generated by Django 5.0.3 on 2024-03-09 14:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('erp', '0006_alter_category_description_alter_type_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='type',
            name='name',
            field=models.CharField(max_length=150, unique=True, verbose_name='Nombre'),
        ),
    ]
