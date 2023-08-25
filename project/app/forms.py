

from django import forms

class CompanySearchForm(forms.Form):
    company_name = forms.CharField(max_length=255, label='Enter Company Name')
