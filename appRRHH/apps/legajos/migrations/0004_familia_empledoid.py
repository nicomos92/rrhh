# Generated by Django 4.1.7 on 2023-03-02 02:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('legajos', '0003_familia_empleado_area_empleado_categoria_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='familia',
            name='empledoID',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='legajos.empleado'),
        ),
    ]
