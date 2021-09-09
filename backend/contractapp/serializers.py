from rest_framework import serializers
from contractapp.models import Contract
from contractapp.models import Event


class ContractSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contract
        fields = ('contract_id', 'customer', 'date_created',
                  'date_updated', 'status', 'amount', 'payment_due')


class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = ('event_id', 'customer', 'date_created',
                  'date_updated', 'attendees', 'event_date', 'notes')
