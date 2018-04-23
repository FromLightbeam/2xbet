from django import forms

import acaunt.user_db_conect as db

class RegistrationForm(forms.Form):
    username = forms.CharField(label='Username', max_length=100)
    name_1 = forms.CharField(label='First name', max_length=100)
    name_2 = forms.CharField(label='Second name', max_length=100)
    password = forms.CharField(label='Password', widget=forms.PasswordInput, max_length=100)
    password_confirmation = forms.CharField(label='Password Confirm', widget=forms.PasswordInput, max_length=100)

    def clean_password_confirmation(self):
        password = self.cleaned_data.get("password")
        confirm_password = self.cleaned_data.get("password_confirmation")
        print(password)
        print(confirm_password)
        if password != confirm_password:
            print("\n\npassword and confirm_password does not match\n\n")
            raise forms.ValidationError(
                "password and confirm_password does not match"
            )
        return confirm_password

    def clean_username(self):
        username = self.cleaned_data.get("username")

        if db.exist_user(username):
            print("\n\nName already exist\n\n")
            raise forms.ValidationError(
                "Name already exist"
            )
        return username


class LoginForm(forms.Form):
    username = forms.CharField(label='Username', max_length=100)
    password = forms.CharField(label='Password', widget=forms.PasswordInput, max_length=100)
