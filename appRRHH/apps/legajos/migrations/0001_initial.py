# Generated by Django 4.1.7 on 2023-03-02 01:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Empleado',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('apellido', models.CharField(max_length=60)),
                ('nombre', models.CharField(max_length=60)),
                ('legajo', models.CharField(max_length=30)),
                ('dni', models.CharField(max_length=30)),
                ('fechaNacimiento', models.DateTimeField()),
                ('fechaIngreso', models.DateTimeField()),
                ('cuit', models.IntegerField()),
                ('telefono', models.IntegerField()),
                ('email', models.CharField(max_length=60)),
            ],
        ),
    ]