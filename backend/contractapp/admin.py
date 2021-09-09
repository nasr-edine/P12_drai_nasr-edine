from django.contrib import admin
from .models import Contract
from .models import Event

# Register your models here.
admin.site.register(Contract)
admin.site.register(Event)
