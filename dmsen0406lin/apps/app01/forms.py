from django import forms
from .models import users

class UserForm(forms.Form):
    # photo = forms.ImageField(label='your photo')
    class Meta:
        model = users
        fields = "__all__"
