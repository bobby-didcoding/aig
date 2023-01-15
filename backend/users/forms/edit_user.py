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
# 3rd Party imports
# --------------------------------------------------------------
from enumfields import EnumField

User = get_user_model()


class EditUserForm(forms.ModelForm):
    
    first_name = forms.CharField(max_length=30, required=True,
      widget=forms.TextInput(attrs={
        'placeholder': 'First name',
        'class': 'form-control'}))

    last_name = forms.CharField(max_length=30, required=True,
      widget=forms.TextInput(attrs={
        'placeholder': 'Last name',
        'class': 'form-control'}))
    
    email = forms.EmailField(max_length=254, required=True,
      widget=forms.EmailInput(attrs={
        'placeholder': 'Email name',
        'class': 'form-control',
        'readonly': 'true'}))
    
    dob = forms.DateTimeField(required=False,
        widget=forms.DateInput(attrs={
            'class': 'form-control',
            'type': 'date'}))
    
    phone_number = forms.CharField(required=False, 
        validators=[
        RegexValidator(
            regex=r'^\+?1?\d{9,15}$', 
            message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed."
            )
        ],
        widget=forms.TextInput(attrs={
        'placeholder': 'Phone number',
        'class': 'form-control'}))

    about = forms.CharField(max_length=500, required=False,
      widget=forms.Textarea(attrs={
        'placeholder': 'Tell us about yourself',
        'class': 'form-control',
        'style':'height: 144px;'}))

    groups = forms.ModelMultipleChoiceField(queryset=Group.objects.all(),required=False)
   
    gender = EnumField(Gender).formfield(required=False)

    class Meta:
        model = User
        fields = ('email',
                  'first_name',
                  'last_name',
                  'gender',
                  'avatar',
                  'dob',
                  'phone_number',
                  'groups',
                  'about',
                )
        widgets = {
            'avatar': forms.FileInput(),
        }
