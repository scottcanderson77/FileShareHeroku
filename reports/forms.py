from django import forms
from django.contrib.auth.models import User, Group

class ReportForm(forms.Form):
    title = forms.CharField()
    timestamp = forms.DateTimeField()
    short_description = forms.CharField(max_length=30)
    detailed_description = forms.CharField(max_length=200)
    status_state = forms.CharField(max_length=10)
    location = forms.CharField(max_length=30)
