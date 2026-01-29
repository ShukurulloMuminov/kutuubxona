from random import choices

from django import forms
from .models import *

class MuallifForm(forms.Form):
    ism = forms.CharField(max_length=50, min_length=3)
    jins = forms.ChoiceField(choices=Muallif.JINS_CHOICES.choices)
    t_sana = forms.DateField(required=False)
    kitob_soni = forms.IntegerField(required=False)
    tirik = forms.BooleanField(required=False)


class KutubxonachiForm(forms.Form):
    ism = forms.CharField(max_length=50, min_length=3)
    ish_vaqti= forms.TimeField(required=False)


class RecordForm(forms.ModelForm):
    class Meta:
        model = Record
        fields = "__all__"
        widgets = {'qaytargan_sana' : forms.DateInput(attrs={'type':'date'})}




class KitobForm(forms.ModelForm):
    class Meta:
        model = Kitob
        fields =  "__all__"

