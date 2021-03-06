from django import forms
from django.contrib.localflavor.us import forms as us_forms
from hackday.users.models import Tshirt, Diet


class SignUpForm(forms.Form):

    user_name = forms.SlugField(label='User Name',
            error_messages={'required': 'Please enter a user name.',
                            'invalid': 'Please enter a user name containing only letters, numbers, underscores, and hyphens.'})
    password = forms.CharField(label='Password', widget=forms.PasswordInput)
    first_name = forms.CharField(label='First Name')
    last_name = forms.CharField(label='Last Name')
    email = forms.EmailField(label='Email Address')
    tshirt = forms.ModelChoiceField(label='T-Shirt Size',
            queryset=Tshirt.objects.all())
    diet = forms.ModelChoiceField(label='Dietary Preference',
            queryset=Diet.objects.all())
    description = forms.CharField(label='Describe Yourself',
            widget=forms.Textarea, required=False)
    notify_by_email = forms.BooleanField(
            label="Email me when there's a new post", required=False)


class SignInForm(forms.Form):

    user_name = forms.SlugField(label='User Name',
            error_messages={'required': 'Please enter a user name.',
                            'invalid': 'Please enter a user name containing only letters, numbers, underscores, and hyphens.'})
    password = forms.CharField(label='Password', widget=forms.PasswordInput)
    next = forms.CharField(label='Next URL', widget=forms.HiddenInput)


class UserProfileForm(forms.Form):

    first_name = forms.CharField(label='First Name')
    last_name = forms.CharField(label='Last Name')
    email = forms.EmailField(label='Email Address')
    tshirt = forms.ModelChoiceField(label='T-Shirt Size',
            queryset=Tshirt.objects.all())
    diet = forms.ModelChoiceField(label='Dietary Preference',
            queryset=Diet.objects.all())
    description = forms.CharField(label='Describe Yourself',
            widget=forms.Textarea, required=False)
    notify_by_email = forms.BooleanField(
            label="Email me when there's a new post", required=False)
    password = forms.CharField(label='Password',
            widget=forms.PasswordInput, required=False)
