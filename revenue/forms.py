from django.forms import ModelForm
from .models import Incoming, Outgoing


class OutgoingForm(ModelForm):
    class Meta:
        model = Outgoing
        fields = ["product_name", "money_spent", "product_image"]

class IncomingForm(ModelForm):
    class Meta:
        model = Incoming
        fields = ["product_name", "money_received", "product_image"]
