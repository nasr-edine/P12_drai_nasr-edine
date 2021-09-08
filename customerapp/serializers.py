from rest_framework import serializers
from customerapp.models import Customer


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ('customer_id', 'first_name', 'last_name', 'email',
                  'phone', 'mobile', 'comapany_name', 'date_created', 'date_updated')
