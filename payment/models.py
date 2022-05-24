from django.contrib.auth.models import User
from django.db import models


# Create your models here.
from django.forms import ModelForm, Select, TextInput


class Payment(models.Model):
    STATUS = (
        ('Yeni', 'Yeni'),
        ('Eksik', 'Eksik'),
        ('Fazla', 'Fazla'),
        ('Tamam', 'Tamam'),
        ('İptal', 'İptal'),
        ('Red', 'Red')
    )
    MONTH = (
        ('Ocak', 'Ocak'),
        ('Şubat', 'Şubat'),
        ('Mart', 'Mart'),
        ('Nisan', 'Nisan'),
        ('Mayıs', 'Mayıs'),
        ('Haziran', 'Haziran'),
        ('Temmuz', 'Temmuz'),
        ('Ağustos', 'Ağustos'),
        ('Eylül', 'Eylül'),
        ('Ekim', 'Ekim'),
        ('Kasım', 'Kasım'),
        ('Aralık', 'Aralık')
    )
    YEAR = (
        (2022, 2022),
        (2023, 2023),
        (2024, 2024),
        (2025, 2025)
    )
    TYPE = (
        ('EFT', 'EFT'),
        ('HAVALE', 'HAVALE'),
        ('KREDİ', 'KREDİ')
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    year = models.IntegerField(choices=YEAR)
    month = models.CharField(max_length=10, choices=MONTH)
    type = models.CharField(max_length=10, choices=TYPE)
    adminnote = models.CharField(blank=True, max_length=100)
    status = models.CharField(max_length=10, choices=STATUS, default='Yeni')
    payment = models.FloatField()
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.subject


class PaymentFormu(ModelForm):
    class Meta:
        model = Payment
        fields = ['year', 'month', 'type', 'payment']
        widgets = {
            'year': Select(attrs={'class': 'input', 'placeholder': 'year'}, choices=Payment.YEAR),
            'month': Select(attrs={'class': 'input', 'placeholder': 'month'}, choices=Payment.MONTH),
            'type': Select(attrs={'class': 'input', 'placeholder': 'type'}, choices=Payment.TYPE),
            'payment': TextInput(attrs={'class': 'input', 'placeholder': 'payment'})
        }
