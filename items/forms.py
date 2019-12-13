from django import forms
from items.models import Page

class PageForm(forms.ModelForm):

    model = Page
    class Meta:
        model = Page
        fields = '__all__'