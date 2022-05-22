from ckeditor_uploader.fields import RichTextUploadingField
from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from django.forms import ModelForm


class Demand(models.Model):
    STATUS = (
        ('New', 'New'),
        ('Accepted', 'Accepted'),
        ('Preparing', 'Preparing'),
        ('Completed', 'Completed'),
        ('Canceled', 'Canceled'),
        ('Refused', 'Refused'),
    )
    TYPE = (
        ('Arıza', 'Arıza'),
        ('Bahçe', 'Bahçe'),
        ('Diğer', 'Diğer'),
        ('Güvenlik', 'Güvenlik'),
        ('Otopark', 'Otopark'),
        ('Sosyal', 'Sosyal'),
        ('Temizlik', 'Temizlik')
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    type = models.CharField(max_length=10, choices=TYPE)
    subject = models.CharField(max_length=50, blank=True)
    detail = RichTextUploadingField(null=True, blank=True)
    adminnote = models.CharField(blank=True, max_length=100)
    status = models.CharField(max_length=10, choices=STATUS, default='New')
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.subject


class DemandFormu(ModelForm):
    class Meta:
        model = Demand
        fields = ['type', 'subject', 'detail']
