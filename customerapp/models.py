from django.db import models

# Create your models here.


class Customer(models.Model):
    # Field name made lowercase.
    customer_id = models.IntegerField(
        db_column='customer_Id', primary_key=True)
    first_name = models.CharField(max_length=25, blank=True, null=True)
    last_name = models.CharField(max_length=25, blank=True, null=True)
    email = models.CharField(max_length=100, blank=True, null=True)
    phone = models.CharField(max_length=20, blank=True, null=True)
    mobile = models.CharField(max_length=20, blank=True, null=True)
    comapany_name = models.CharField(max_length=250, blank=True, null=True)
    date_created = models.DateTimeField(blank=True, null=True)
    date_updated = models.DateTimeField(blank=True, null=True)
