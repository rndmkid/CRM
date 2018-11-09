from django import forms
from django.contrib.auth.forms import AuthenticationForm

from .models import Account
from django.contrib.auth import get_user_model

class AccountForm(forms.ModelForm):
    class Meta:
        model = Account
        fields = ('name', 'desc', 'address_one',
                  'address_two', 'city', 'state', 'phone',
        )
        widgets = {
            'name': forms.TextInput(
                attrs={
                    'placeholder':'Company',
                    'class':'col-md-12 form-control'
                }
            ),
            'desc': forms.Textarea(
                attrs={
                    'placeholder':'Enter a description',
                    'class':'form-control'
                }
            ),
            'address_one': forms.TextInput(
                attrs={
                    'placeholder':'Street Address',
                    'class':'gi-form-addr form-control'
                }
            ),
            'address_two': forms.TextInput(
                attrs={
                    'placeholder':'Suite, PO, etc',
                    'class':'gi-form-addr form-control'
                }
            ),
            'city': forms.TextInput(
                attrs={
                    'placeholder':'City',
                    'class':'gi-form-addr form-control'
                }
            ),
            'state': forms.TextInput(
                attrs={
                    'placeholder':'State',
                    'class':'gi-form-addr form-control'
                }
            ),
            'phone': forms.TextInput(
                attrs={
                    'placeholder':'Phone',
                    'class':'gi-form-addr form-control'
                }
            ),
        }

class CustomAuthenticationForm(AuthenticationForm):

    def authenticate(self, request, username, password, **kwargs):
        UserModel = get_user_model()
        try:
            out = UserModel.objects.get(username=username,
                                        password=password)
            return out
        except:
            return None
    
    def clean(self):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')

        if username is not None and password:
            self.user_cache = self.authenticate(self.request,
                                           username=username,
                                           password=password)
            if self.user_cache is None:
                raise self.get_invalid_login_error()
            else:
                self.confirm_login_allowed(self.user_cache)

        return self.cleaned_data
