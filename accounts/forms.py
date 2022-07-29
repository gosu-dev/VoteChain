from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import ModelForm


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password1']

    def __init__(self, *args, **kwargs):
        super(CustomUserCreationForm, self).__init__(self, *args, **kwargs)
        self.fields['username'].widget.attrs.update({'class': 'form-control'})
