# Generated by Django 4.0.3 on 2022-04-10 23:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0003_content'),
    ]

    operations = [
        migrations.AlterField(
            model_name='content',
            name='title',
            field=models.CharField(max_length=150),
        ),
        migrations.AlterField(
            model_name='menu',
            name='title',
            field=models.CharField(max_length=100),
        ),
        migrations.CreateModel(
            name='Imagen',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('image', models.ImageField(blank=True, upload_to='images/')),
                ('content', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='content.content')),
            ],
        ),
    ]
