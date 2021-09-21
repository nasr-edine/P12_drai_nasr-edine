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
        # print(self.context['request'].user)
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
                {"this sales contact is not recorded as a member with sales role"})
        sales_contact = data['sales_contact']
        queryset = sales_contact.customers.all()
        print(self)
        if not data['customer'] in queryset:
            raise serializers.ValidationError(
                {"this customer is not created by the sales contact"})
        return data

    class Meta:
        model = Contract
        fields = ('contract_id', 'customer', 'date_created',
                  'date_updated', 'status', 'amount', 'payment_due', 'sales_contact')
        # read_only_fields = ['sales_contact']


class ContractUpdateSerializer(serializers.ModelSerializer):
    # def validate(self, data):
    #     print(self.context['request'].user)
    #     sales_contact = self.context['request'].user
    #     queryset = sales_contact.customers.all()
    #     if not data['customer'] in queryset:
    #         raise serializers.ValidationError(
    #             {"this customer is not created by the sales contact"})
    #     return data

    class Meta:
        model = Contract
        fields = ('contract_id', 'customer', 'date_created',
                  'date_updated', 'status', 'amount', 'payment_due', 'sales_contact')
        read_only_fields = ['sales_contact', 'customer']


class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = ('event_id', 'contract', 'date_created',
                  'date_updated', 'attendees', 'event_date', 'notes', 'support_contact')


class EventCreateSerializer(serializers.ModelSerializer):
    def validate(self, data):

        # check if the contract for this event is signed
        status_contract = data['contract'].status
        if status_contract == False:
            raise serializers.ValidationError(
                {"You cannot create an event for this contract because it is not signed"})
        # check if the request user is the sales contact the contract field
        contact = self.context['request'].user
        customer = data['contract'].customer
        queryset = contact.customers.all()
        if not customer in queryset:
            raise serializers.ValidationError(
                {"You are not the sales contact for this contract"})

        # check if the support contact exisit in member table with support role
        queryset = Member.objects.filter(role='support')
        if not data['support_contact'] in queryset:
            raise serializers.ValidationError(
                {"this contact is not a member with support role"})
        return data

    class Meta:
        model = Event
        fields = ('event_id', 'contract', 'date_created',
                  'date_updated', 'attendees', 'event_date', 'notes', 'support_contact')


class EventCreateSerializerManager(serializers.ModelSerializer):
    def validate(self, data):
       # check if the contract for this event is signed
        status_contract = data['contract'].status
        if status_contract == False:
            raise serializers.ValidationError(
                {"You cannot create an event for this contract because it is not signed"})

        # check if the  is the sales contact the contract field
        # contact = self.context['request'].user
        # customer = data['contract'].customer
        # queryset = contact.customers.all()
        # if not customer in queryset:
        #     raise serializers.ValidationError(
        #         {"You are not the sales contact for this contract"})

        # check if the support contact exisit in member table with support role
        queryset = Member.objects.filter(role='support')
        if not data['support_contact'] in queryset:
            raise serializers.ValidationError(
                {"this contact is not a member with support role"})
        return data

    class Meta:
        model = Event
        fields = ('event_id', 'contract', 'date_created',
                  'date_updated', 'attendees', 'event_date', 'notes', 'support_contact')
