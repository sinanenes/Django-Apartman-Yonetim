# Generated by Django 4.0.3 on 2022-05-27 20:12

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0009_setting_pinterest_alter_setting_facebook_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='blok',
            field=models.CharField(choices=[('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D')], default='A', max_length=150),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='userprofile',
            name='daire',
            field=models.IntegerField(default=1, validators=[django.core.validators.MaxValueValidator(100), django.core.validators.MinValueValidator(1)]),
            preserve_default=False,
        ),
    ]
