# Generated by Django 4.0.3 on 2022-05-14 16:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0008_alter_comment_rate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='content',
            name='slug',
            field=models.SlugField(unique=True),
        ),
        migrations.AlterField(
            model_name='menu',
            name='slug',
            field=models.SlugField(unique=True),
        ),
    ]
