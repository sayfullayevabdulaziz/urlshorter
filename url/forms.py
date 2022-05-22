from django import forms
from .models import UrlModel, ReportLinkModel, ContactModel


class UrlForm(forms.ModelForm):
    class Meta:
        model = UrlModel
        fields = ['url']

class UrlCounterForm(forms.Form):
    url = forms.CharField(max_length=300)


    def clean_url(self):
        url = self.cleaned_data['url']
        if not 'localhost' in url:
            raise forms.ValidationError('Url is incorrect')
        return url


class ReportForm(forms.ModelForm):
    result = forms.CharField(required=True)

    class Meta:
        model = ReportLinkModel
        fields = ['url','comment']

    
class ContactForm(forms.ModelForm):
    result = forms.CharField(required=True)

    class Meta:
        model = ContactModel
        fields = ['name', 'email', 'message']