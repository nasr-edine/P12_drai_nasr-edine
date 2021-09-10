from staff.models import Member
from django.db import models
from customerapp.models import Customer
# Create your models here.


class Contract(models.Model):
    contract_id = models.BigAutoField(primary_key=True)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    status = models.BooleanField(blank=True, null=True)
    amount = models.FloatField(blank=True, null=True)
    payment_due = models.DateTimeField(blank=True, null=True)
    sales_contact = models.ForeignKey(Member, on_delete=models.CASCADE)

    def __str__(self):
        # return a contract
        return 'contract \u2116: %d, %s' % (self.customer_id, self.customer)


class Event(models.Model):
    event_id = models.BigAutoField(primary_key=True)
    contract = models.OneToOneField(Contract, on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    # event_status = models.IntegerField(blank=True, null=True)
    attendees = models.IntegerField(blank=True, null=True)
    event_date = models.DateTimeField(blank=True, null=True)
    notes = models.TextField(max_length=2048, blank=True, null=True)
    support_contact = models.ForeignKey(Member, on_delete=models.CASCADE)
