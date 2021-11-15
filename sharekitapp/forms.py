from django import forms
from nepse_func import companies


class Ipo(forms.Form):
    company = forms.ChoiceField(label="Company: ", choices=companies)
