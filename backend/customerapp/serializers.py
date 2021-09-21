from rest_framework import serializers

from customerapp.models import Customer
from staff.models import Member


class CustomerSerializer(serializers.ModelSerializer):
    def validate(self, data):
        print('validate called')
        if self.context['request'].user == 'management' or self.context['request'].user.is_superuser:
            queryset = Member.objects.filter(role='sales')
            if not data['sales_contact'] in queryset:
                raise serializers.ValidationError(
                    {"this sales contact is not recorded as a member with sales role"})
        return data

    class Meta:
        model = Customer
        fields = ('customer_id', 'first_name', 'last_name', 'email', 'phone',
                  'mobile', 'company_name', 'date_created', 'date_updated', 'sales_contact', 'is_prospect')


class CustomerCreateSerializerBySalesMan(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ('customer_id', 'first_name', 'last_name', 'email', 'phone',
                  'mobile', 'company_name', 'is_prospect', 'sales_contact')
        read_only_fields = ['sales_contact']


class CustomerUpdateSerializerManager(serializers.ModelSerializer):
    sales_contact = serializers.PrimaryKeyRelatedField(
        required=False, queryset=Member.objects.all())

    def validate(self, data):
        queryset = Member.objects.filter(role='sales')
        if 'sales_contact' in data:
            if not data['sales_contact'] in queryset:
                raise serializers.ValidationError(
                    {"this sales contact is not recorded as a member with sales role"})
            return data
        return data

    class Meta:
        model = Customer
        fields = ('customer_id', 'first_name', 'last_name', 'email', 'phone',
                  'mobile', 'company_name', 'date_created', 'date_updated', 'sales_contact', 'is_prospect')
