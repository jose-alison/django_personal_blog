from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from .models import User

class UserCreateForm(UserCreationForm):
    email = forms.EmailField(required=True)
    first_name = forms.CharField(max_length=30, required=False)
    last_name = forms.CharField(max_length=30, required=False)

    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name', 'password1', 'password2', 'is_reader', 'is_publisher')

class UserUpdateForm(UserChangeForm):
    first_name = forms.CharField(max_length=30, required=False)
    last_name = forms.CharField(max_length=30, required=False)

    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name', 'is_reader', 'is_publisher',)
    
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].disabled = True
        self.fields['email'].disabled = True
    
