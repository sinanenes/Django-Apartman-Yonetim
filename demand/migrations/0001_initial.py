# Generated by Django 4.0.3 on 2022-05-22 21:06

import ckeditor_uploader.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Demand',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[('Arıza', 'Arıza'), ('Bahçe', 'Bahçe'), ('Diğer', 'Diğer'), ('Güvenlik', 'Güvenlik'), ('Otopark', 'Otopark'), ('Sosyal', 'Sosyal'), ('Temizlik', 'Temizlik')], max_length=10)),
                ('subject', models.CharField(blank=True, max_length=50)),
                ('detail', ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True)),
                ('adminnote', models.CharField(blank=True, max_length=100)),
                ('status', models.CharField(choices=[('New', 'New'), ('Accepted', 'Accepted'), ('Preparing', 'Preparing'), ('Completed', 'Completed'), ('Canceled', 'Canceled'), ('Refused', 'Refused')], default='New', max_length=10)),
                ('create_at', models.DateTimeField(auto_now_add=True)),
                ('update_at', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
