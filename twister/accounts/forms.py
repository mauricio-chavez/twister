"""Accounts forms for twister project."""

from django import forms
from django.contrib.auth.models import User

from .models import Profile


class SignupForm(forms.Form):
    """Form to register accounts."""
    username = forms.CharField(min_length=3, max_length=150)
    email = forms.EmailField(
        widget=forms.EmailInput()
    )
    first_name = forms.CharField(max_length=30)
    last_name = forms.CharField(max_length=150)
    password = forms.CharField(
        min_length=5,
        max_length=128,
        widget=forms.PasswordInput()
    )
    password_confirmation = forms.CharField(
        min_length=5,
        max_length=128,
        widget=forms.PasswordInput()
    )

    def clean_username(self):
        """Username must be unique."""
        username = self.cleaned_data['username']
        username_taken = User.objects.filter(username=username).exists()
        if username_taken:
            if username == 'oneaboveall':
                raise forms.ValidationError(
                    f'You cannot be me!'
                )
            raise forms.ValidationError(
                f'@{ username } is already in use.'
            )
        return username

    def clean(self):
        """Passwords must match."""
        data = super().clean()

        password = data['password'] if 'password' in data else None
        password_confirmation = data['password_confirmation'] \
            if 'password_confirmation' in data else None

        if password and password_confirmation and password != password_confirmation:
            raise forms.ValidationError('Passwords do not match.')

        return data

    def save(self):
        """Create user and profile."""
        data = self.cleaned_data
        data.pop('password_confirmation')

        username = data['username']

        user = User.objects.create_user(**data)
        Profile.objects.create(user=user, display_name=username)
        # profile.save()
