# Generated by Django 4.0.3 on 2022-04-30 23:23

import ckeditor_uploader.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0004_alter_content_title_alter_menu_title_imagen'),
    ]

    operations = [
        migrations.AlterField(
            model_name='content',
            name='detail',
            field=ckeditor_uploader.fields.RichTextUploadingField(),
        ),
    ]
