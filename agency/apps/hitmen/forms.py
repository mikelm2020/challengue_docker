from django import forms
from django.contrib.auth import authenticate

from .models import User


class UserRegisterForm(forms.ModelForm):

    password = forms.CharField(
        label="Password",
        required=True,
        widget=forms.PasswordInput(
            attrs={
                "placeholder": "Password",
                "class": "input-group-field",
            }
        ),
    )
    repeat_password = forms.CharField(
        label="Password",
        required=True,
        widget=forms.PasswordInput(
            attrs={
                "placeholder": "Repeat Password",
                "class": "input-group-field",
            }
        ),
    )

    class Meta:
        """Meta definition for UserRegisterform."""

        model = User

        fields = (
            "name",
            "email",
        )
        widgets = {
            "name": forms.TextInput(
                attrs={
                    "placeholder": "Name ...",
                    "class": "input-group-field",
                }
            ),
            "email": forms.EmailInput(
                attrs={
                    "placeholder": "Email ...",
                    "class": "input-group-field",
                }
            ),
        }

    def clean_repeat_password(self):
        if self.cleaned_data["password"] != self.cleaned_data["repeat_password"]:
            self.add_error("repeat_password", "Passwords are not the same")


class LoginForm(forms.Form):
    email = forms.CharField(
        label="E-mail",
        required=True,
        widget=forms.TextInput(
            attrs={
                "class": "input-group-field",
                "placeholder": "Email",
            }
        ),
    )
    password = forms.CharField(
        label="Password",
        required=True,
        widget=forms.PasswordInput(
            attrs={"class": "input-group-field", "placeholder": "password"}
        ),
    )

    def clean(self):
        cleaned_data = super(LoginForm, self).clean()
        email = self.cleaned_data["email"]
        password = self.cleaned_data["password"]

        if not authenticate(email=email, password=password):
            raise forms.ValidationError("The user data is not correct")
        return self.cleaned_data


class UserUpdateForm(forms.ModelForm):
    class Meta:

        model = User
        fields = (
            "email",
            "name",
            "description",
            "status",
            "manager",
        )
        widgets = {
            "email": forms.EmailInput(
                attrs={
                    
                    "placeholder": "Email ...",
                    "class": "input-group-field",
                }
            ),
            "name": forms.TextInput(
                attrs={
                    
                    "placeholder": "Name ...",
                    "class": "input-group-field",
                }
            ),
            "description": forms.TextInput(
                attrs={
                    
                    "placeholder": "Description ...",
                    "class": "input-group-field",
                }
            ),
            "status": forms.Select(
                attrs={
                    "placeholder": "Status ...",
                    "class": "input-group-field",
                }
            ),
            "manager": forms.Select(
                attrs={
                    
                    "placeholder": "Manager ...",
                    "class": "input-group-field",
                }
            ),
        }


class UpdatePasswordForm(forms.Form):

    current_password = forms.CharField(
        label="Current Password",
        required=True,
        widget=forms.PasswordInput(attrs={"placeholder": "Current password"}),
    )
    new_password = forms.CharField(
        label="New Password",
        required=True,
        widget=forms.PasswordInput(attrs={"placeholder": "New password"}),
    )
