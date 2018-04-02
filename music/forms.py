from django.contrib.auth.models import User
from django import forms


class UserForm(forms.ModelForm):
	password = forms.CharField(widget=forms.PasswordInput) #show password into steric

	class Meta:
		model = User
		fields = ['username', 'first_name', 'email', 'password']
