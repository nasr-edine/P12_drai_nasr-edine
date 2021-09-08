from django.db import models
from customerapp.models import Customer
# Create your models here.


class Contract(models.Model):
    contract_id = models.IntegerField(
        db_column='contract_id', primary_key=True)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    date_created = models.DateTimeField(blank=True, null=True)
    date_updated = models.DateTimeField(blank=True, null=True)
    status = models.BooleanField(blank=True, null=True)
    amount = models.FloatField(blank=True, null=True)
    payment_due = models.DateTimeField(blank=True, null=True)


class Event(models.Model):
    event_id = models.IntegerField(primary_key=True)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    date_reated = models.DateTimeField(blank=True, null=True)
    date_updated = models.DateTimeField(blank=True, null=True)
    event_status = models.IntegerField(blank=True, null=True)
    attendees = models.IntegerField(blank=True, null=True)
    event_date = models.DateTimeField(blank=True, null=True)
    notes = models.TextField(blank=True, null=True)
