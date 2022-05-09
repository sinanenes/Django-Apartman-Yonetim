from django import forms


class SearchFormu(forms.Form):
    query = forms.CharField(label='Search', max_length=100)
