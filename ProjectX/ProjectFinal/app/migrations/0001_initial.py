# Generated by Django 4.2.2 on 2023-09-20 20:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='RegistroEmpresas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=600)),
                ('direccion', models.CharField(max_length=600)),
                ('telefono', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='RegistroEvento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=600)),
                ('fecha', models.DateField()),
                ('horario', models.TimeField()),
                ('lugar', models.CharField(max_length=600)),
            ],
        ),
        migrations.CreateModel(
            name='RegistroLuchadores',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=600)),
                ('edad', models.IntegerField()),
                ('peso', models.FloatField()),
            ],
        ),
    ]
