# Generated by Django 3.0.5 on 2021-06-09 00:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_denuncias', '0002_auto_20210603_1703'),
    ]

    operations = [
        migrations.AlterField(
            model_name='denuncias',
            name='latitude',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='denuncias',
            name='logintude',
            field=models.FloatField(),
        ),
    ]
