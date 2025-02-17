from django import forms
from django.contrib.auth.password_validation import validate_password


class UserLoginForm(forms.Form):
    username = forms.CharField()
        #widget=forms.CharField(
            #attrs={'class': 'form-control', 'placeholder': 'username'}
        #)
    #)
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={'class': 'form-control', 'placeholder': 'password'}
        )
    )

class UserRegisterForm(forms.Form):

    first_name = forms.CharField()

    last_name = forms.CharField()
    
    phone = forms.CharField()

    email = forms.EmailField(
        widget=forms.EmailInput(
        attrs={'class': 'form-control', 'placeholder': 'email'}
    )
)
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={'class': 'form-control', 'placeholder': 'password'}
        )
    )
    repeated_password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={'class': 'form-control', 'placeholder': 'repeated_password'}
        )
    )   

    def clean_password(self):
        password = self.cleaned_data.get('password')
        validate_password(password)
        return password
    

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        repeated_password = cleaned_data.get('repeated_password')

        if password != repeated_password:
            raise forms.ValidationError("Passwords do not match.")