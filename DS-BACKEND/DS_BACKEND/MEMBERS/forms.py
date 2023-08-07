from django.forms import ModelForm
from django import forms
from .models import *

class MemberCreationForm(forms.ModelForm):
    class Meta:
        model = Member
        fields = ('firstname', 'lastname', 'passout_year', 'post', 'dp', 'instagram_url','linkedin_url','facebook_url','github_url')