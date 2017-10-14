from django import forms
from django.core import validators
from .models import myUser
from .models import UserProfileInfo
from django.contrib.auth.forms import User

def my_validator_check_for_z(value):
    if value[0].lower() != 'z':
        raise forms.ValidationError("needs to start with z")

# class UserForm(forms.ModelForm):
#     class Meta():
#         model = myUser
#         fields = "__all__"

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta():
        model = User
        fields = ('username', 'email', 'password')

class UserProfileInfoForm(forms.ModelForm):
    # portfolio = forms.URLField(required=False)
    # picture = forms.ImageField(required=False)

    class Meta():
        model = UserProfileInfo
        fields = ('portfolio', 'picture')



# # a normal form, not conneccted to model
# class UserForm(forms.Form):
#     name = forms.CharField(validators=[my_validator_check_for_z])
#     email = forms.EmailField()
#     verify_email = forms.EmailField(label="please enter your email again")
#     text = forms.CharField(widget=forms.Textarea)
#     # botcatcher = forms.CharField(required=False,
#     #                              widget=forms.HiddenInput,
#     #                              validators=[validators.MaxLengthValidator(0)])
#
#     def clean(self):
#         all_clean_data = super().clean()
#         email = all_clean_data['email']
#         verify_email = all_clean_data['verify_email']
#         if email != verify_email:
#             raise forms.ValidationError("email is not equal in both fields")