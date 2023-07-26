from django import forms
from publications.models import Publications


class PublicationsForm(forms.ModelForm):
    class Meta:
        model = Publications
        fields = ['discriptions', 'photo']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class': 'form-control'
            })