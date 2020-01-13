from django import forms
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login


class LoginForm(forms.Form):
    username = forms.CharField(label="Username")
    password = forms.CharField(label='Password', widget=forms.PasswordInput())

    def log(self, request):
        username = self.cleaned_data['username']
        password = self.cleaned_data['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
        return user


class SingUpForm(forms.ModelForm):
    password = forms.CharField(
        label='Password',
        widget=forms.PasswordInput(),
    )
    password2 = forms.CharField(
        label='Re-Enter Password',
        widget=forms.PasswordInput(),
    )

    class Meta:
        model = User
        fields = ("first_name", "last_name", "email", "username", "password")

    def clean_password2(self):
        password = self.cleaned_data['password']
        password2 = self.cleaned_data['password2']
        if password != password2:
            raise forms.ValidationError("Invalid Password...!")
        return password2

    def save(self, commit=True):
        user = super().save(commit=False)
        password = self.cleaned_data['password']
        user.set_password(password)
        if commit:
            user.save()
        return user
