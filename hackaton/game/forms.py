from django import forms

from .models import *


class PaladinForm(forms.ModelForm):
    class Meta:
        model = Paladin
        fields = ('name', 'nick_name', 'image')


class WarriorForm(forms.ModelForm):
    class Meta:
        model = Warrior
        fields = ('name', 'nick_name', 'image')


class DruidForm(forms.ModelForm):
    class Meta:
        model = Druid
        fields = ('name', 'nick_name', 'image')


class ThingsForm(forms.ModelForm):
    class Meta:
        model = Things
        fields = ('owners', 'name_class', 'name',
                  'thing_armor', 'thing_stamina', 'thing_strength')
