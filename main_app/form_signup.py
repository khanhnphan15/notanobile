from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UsernameField


class SignupForm(UserCreationForm):
    class Meta:
        model = User
        fields = ("username", "first_name", "last_name",)
        field_classes = {"username": UsernameField}

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
            if hasattr(self, "save_m2m"):
                self.save_m2m()
        return user
