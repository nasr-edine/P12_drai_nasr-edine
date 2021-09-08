from django.db import models

# Create your models here.


class Customer(models.Model):
    # Field name made lowercase.
    customer_id = models.BigAutoField(primary_key=True)
    first_name = models.CharField(max_length=25, blank=True, null=True)
    last_name = models.CharField(max_length=25, blank=True, null=True)
    email = models.CharField(max_length=100, blank=True, null=True)
    phone = models.CharField(max_length=20, blank=True, null=True)
    mobile = models.CharField(max_length=20, blank=True, null=True)
    comapany_name = models.CharField(max_length=250, blank=True, null=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        # return self.title
        return 'customer \u2116 %d: %s %s' % (self.customer_id, self.first_name, self.last_name)
