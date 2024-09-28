from django import forms
from .models import NewsletterUser
from .models import Newsletter


class NewsletterUserSignUp(forms.ModelForm):
    class Meta:
        model = NewsletterUser
        fields = ['email']


class NewsletterCreationForm(forms.ModelForm):
    class Meta:
        model = Newsletter
        fields = ['name','subject','body','email']