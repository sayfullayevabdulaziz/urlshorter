# Generated by Django 4.0.4 on 2022-05-22 08:14

from django.db import migrations, models
import url.models


class Migration(migrations.Migration):

    dependencies = [
        ('url', '0006_alter_reportlinkmodel_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reportlinkmodel',
            name='url',
            field=models.CharField(max_length=300, validators=[url.models.validate_url]),
        ),
    ]
