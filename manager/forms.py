from django.forms import ModelForm
from .models import PasswordModel


class PasswordModelForm(ModelForm):
    class Meta:
        model = PasswordModel
        exclude = ('user',)
