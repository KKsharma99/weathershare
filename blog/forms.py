from django import forms

class LookupWeatherForm(forms.Form):
    post = forms.CharField()