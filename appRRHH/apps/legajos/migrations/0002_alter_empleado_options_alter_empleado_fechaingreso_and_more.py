# Generated by Django 4.1.7 on 2023-03-02 02:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('legajos', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='empleado',
            options={'verbose_name': 'Empleado', 'verbose_name_plural': 'Empleados'},
        ),
        migrations.AlterField(
            model_name='empleado',
            name='fechaIngreso',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='empleado',
            name='fechaNacimiento',
            field=models.DateField(),
        ),
    ]
