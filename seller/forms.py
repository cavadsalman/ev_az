from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

class RegisterForm(forms.ModelForm):
    password2 = forms.CharField(max_length=100, widget=forms.PasswordInput, label='Password Again')
    password = forms.CharField(max_length=100, widget=forms.PasswordInput, label='Password Again')
    def clean(self):
        data = self.cleaned_data
        if 'password' in data and 'password2' in data:
            if data.get('password') != data.get('password2'):
                raise ValidationError('Sifreler eyni deyil', code='not-same-password')
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'password', 'email']