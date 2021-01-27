from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile

class UserRegisterForm(UserCreationForm):
    #UserRegisterForm inherited from UserCreationForm, we want to add email to the form
    #UserCreationForm is a default django form imported from django.contrib.auth.forms
    email = forms.EmailField()

    class Meta:
        #inside the Mega, we indicate which model we want to interacte with, which in --
        # -- this case is the User
        model = User
        #what fields we want to put on the form and in which order
        #password1 is the password, password2 is the password confirm
        fields = ['username', 'email', 'password1', 'password2']

# After creating the UserRegisterForm, we can then import to views.py--
# -- using this code: from .forms import UserRegisterForm

class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()
    class Meta:
        model = User
        fields = ['username', 'email']

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image']
