from accounts.models import User
from django import forms


class ProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'email','phone','bio', 'image', 'country')