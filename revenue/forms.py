from django.forms import ModelForm
from .models import Expenditure


class SignUpForm(ModelForm):
    class Meta:
        model = Expenditure
        fields = '__all__'
