# Generated by Django 5.0.3 on 2024-03-09 00:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('erp', '0004_type_alter_employee_table_employee_type'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, verbose_name='Nombre')),
                ('description', models.TextField(max_length=500, verbose_name='Descripción')),
            ],
            options={
                'verbose_name': 'Categoría',
                'verbose_name_plural': 'Categorías',
                'ordering': ['id'],
            },
        ),
        migrations.AddField(
            model_name='employee',
            name='category',
            field=models.ManyToManyField(to='erp.category', verbose_name='Categorías'),
        ),
    ]