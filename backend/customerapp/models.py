from django.db import models

from staff.models import Member


class Customer(models.Model):
    customer_id = models.BigAutoField(primary_key=True)
    first_name = models.CharField(max_length=25, blank=True, null=True)
    last_name = models.CharField(max_length=25, blank=True, null=True)
    email = models.CharField(max_length=100, blank=True, null=True)
    phone = models.CharField(max_length=20, blank=True, null=True)
    mobile = models.CharField(max_length=20, blank=True, null=True)
    comapany_name = models.CharField(max_length=250, blank=True, null=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    sales_contact = models.ForeignKey(Member, on_delete=models.CASCADE)

    def __str__(self):
        # return 'customer \u2116 %d: %s %s' % (self.customer_id, self.first_name, self.last_name)
        return '%s %s' % (self.first_name, self.last_name)
