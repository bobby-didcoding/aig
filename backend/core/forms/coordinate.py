# --------------------------------------------------------------
# Django imports
# --------------------------------------------------------------
from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group

# --------------------------------------------------------------
# Project imports
# --------------------------------------------------------------
from utils.fields.enums import Gender
from utils.validators import RegexValidator

# --------------------------------------------------------------
# app imports
# --------------------------------------------------------------
from core.models.coordinate import Coordinate

# --------------------------------------------------------------
# 3rd Party imports
# --------------------------------------------------------------
from enumfields import EnumField


class CoordinateForm(forms.ModelForm):
    
    x = forms.CharField(max_length=30, required=True,
      widget=forms.TextInput(attrs={
        'placeholder': 'X',
        'class': 'form-control'}))

    y = forms.CharField(max_length=30, required=True,
      widget=forms.TextInput(attrs={
        'placeholder': 'Y',
        'class': 'form-control'}))

    x2 = forms.CharField(max_length=30, required=True,
      widget=forms.TextInput(attrs={
        'placeholder': 'X2',
        'class': 'form-control'}))

    class Meta:
        model = Coordinate
        fields = ('x',
                  'y',
                  'x2',
                  'y2',
                )
