from staff.models import Member
from django.db import models
from customerapp.models import Customer
# Create your models here.


class Contract(models.Model):
    contract_id = models.BigAutoField(primary_key=True)
    customer = models.ForeignKey(
        Customer, related_name='contracts', on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    status = models.BooleanField(blank=True, null=True)
    amount = models.FloatField(blank=True, null=True)
    payment_due = models.DateTimeField(blank=True, null=True)
    sales_contact = models.ForeignKey(Member, on_delete=models.CASCADE)

    def __str__(self):
        return 'contract \u2116: %d, %s' % (self.contract_id, self.customer.full_name)


STATUS_CHOICES = [
    ('progress', 'progress'),
    ('finished', 'finished'),
]


class Event(models.Model):
    event_id = models.BigAutoField(primary_key=True)
    contract = models.OneToOneField(
        Contract, related_name='event', on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    event_status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        blank=True,
        default="progress")
    attendees = models.IntegerField(blank=True, null=True)
    event_date = models.DateTimeField(blank=True, null=True)
    notes = models.TextField(max_length=512, blank=True, null=True)
    support_contact = models.ForeignKey(
        Member, related_name='events', on_delete=models.CASCADE)

    def __str__(self):
        return 'event \u2116: %d, %s' % (self.event_id, self.contract.customer.full_name)
