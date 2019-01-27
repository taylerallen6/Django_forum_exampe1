from django import forms
from django.contrib.auth import get_user_model


class PostForm(forms.Form):
	body = forms.CharField(max_length=300, widget=forms.TextInput(
                    attrs={
                        "class": "form-control", 
                        "placeholder": "Enter post here"
                    }))