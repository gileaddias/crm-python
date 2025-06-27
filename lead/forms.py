from django import forms

from .models import Lead

class AddLeadForms(forms.ModelForm):
    class Meta:

        model = Lead
        fields = ('name', 'email', 'description', 'priority', 'status')