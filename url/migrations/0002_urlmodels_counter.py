# Generated by Django 4.0.4 on 2022-05-19 08:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('url', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='urlmodels',
            name='counter',
            field=models.IntegerField(default=0),
        ),
    ]
