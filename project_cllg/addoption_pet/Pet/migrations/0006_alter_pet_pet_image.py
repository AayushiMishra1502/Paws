# Generated by Django 4.0.1 on 2022-01-08 00:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Pet', '0005_pet_pet_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pet',
            name='pet_image',
            field=models.ImageField(blank=True, default='', null=True, upload_to='Pet_pic'),
        ),
    ]
