# from django import forms
# from .models import ShortURL

# class CreateNewShortURL(forms.ModelForm):
#     class Meta:
#         model = ShortURL

#     fields = {
#         'original_url',
#     }

#     widgets = {
#         'original_url': forms.TextInput(attrs={'class': 'form-control'})
#     }


from .models import ShortURL
from django import forms

class CreateNewShortURL(forms.ModelForm):
    class Meta:
        model=ShortURL
        fields = {'original_url'}

        widgets = {
            'original_url': forms.TextInput(attrs={'class': 'form-control'})
        }
