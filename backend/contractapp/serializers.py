from rest_framework import serializers
from contractapp.models import Contract
from contractapp.models import Event
from staff.models import Member


class ContractSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contract
        fields = ('contract_id', 'customer', 'date_created',
                  'date_updated', 'status', 'amount', 'payment_due', 'sales_contact')


class ContractCreateSerializer(serializers.ModelSerializer):
    def validate(self, data):
        print(self.context['request'].user)
        sales_contact = self.context['request'].user
        queryset = sales_contact.customers.all()
        if not data['customer'] in queryset:
            raise serializers.ValidationError(
                {"this customer is not created by the sales contact"})
        return data

    class Meta:
        model = Contract
        fields = ('contract_id', 'customer', 'date_created',
                  'date_updated', 'status', 'amount', 'payment_due', 'sales_contact')
        read_only_fields = ['sales_contact']


class ContractCreateSerializerManager(serializers.ModelSerializer):
    def validate(self, data):
        queryset = Member.objects.filter(role='sales')
        if not data['sales_contact'] in queryset:
            raise serializers.ValidationError(
                {"this sales contact is not recored as a member with sales role"})
        print(data['sales_contact'])
        sales_contact = data['sales_contact']
        queryset = sales_contact.customers.all()
        if not data['customer'] in queryset:
            raise serializers.ValidationError(
                {"this customer is not created by the sales contact"})
        return data

    class Meta:
        model = Contract
        fields = ('contract_id', 'customer', 'date_created',
                  'date_updated', 'status', 'amount', 'payment_due', 'sales_contact')


class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = ('event_id', 'contract', 'date_created',
                  'date_updated', 'attendees', 'event_date', 'notes', 'support_contact')
