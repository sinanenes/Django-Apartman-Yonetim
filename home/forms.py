from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class SearchFormu(forms.Form):
    query = forms.CharField(label='Search', max_length=100)
    menuid = forms.IntegerField()


class SignUpFormu(UserCreationForm):
    username = forms.CharField(max_length=30, label='User Name', help_text='Kullanıcı Adı')
    email = forms.EmailField(max_length=200, label='Email ', help_text='E-posta')
    first_name = forms.CharField(max_length=100, label='First Name', help_text='Ad')
    last_name = forms.CharField(max_length=100, label='Last Name', help_text='Soyad')

    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name', 'password1', 'password2',)
