# Generated by Django 5.0 on 2023-12-15 19:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('carreras', '0003_alter_carrera_url_img'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comision',
            name='numero',
        ),
        migrations.AddField(
            model_name='comision',
            name='codigo',
            field=models.CharField(default='', max_length=30),
        ),
        migrations.AddField(
            model_name='comision',
            name='cupo',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='alumno',
            name='dni',
            field=models.CharField(default='', max_length=20),
        ),
        migrations.AlterField(
            model_name='carrera',
            name='duracion',
            field=models.IntegerField(default=0),
        ),
    ]
