from django.contrib import admin
from .models import Incoming, Outgoing

# Register your models here.
admin.site.register(Outgoing)
admin.site.register(Incoming)
