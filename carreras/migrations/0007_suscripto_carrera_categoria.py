# Generated by Django 4.2.7 on 2023-12-19 16:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('carreras', '0006_alumno_email'),
    ]

    operations = [
        migrations.CreateModel(
            name='Suscripto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('suscripto', models.EmailField(default='alumno@gmail.com', max_length=254)),
            ],
        ),
        migrations.AddField(
            model_name='carrera',
            name='categoria',
            field=models.CharField(default='', max_length=120),
        ),
    ]
