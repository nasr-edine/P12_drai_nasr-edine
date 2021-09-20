# from staff.models import Member
# from typing_extensions import Required
from staff.models import Member
from django.contrib.auth import models
from django.db.models.fields import IntegerField
from rest_framework import serializers
from customerapp.models import Customer

from staff.serializers import MemberSerializer


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ('customer_id', 'first_name', 'last_name', 'email', 'phone',
                  'mobile', 'company_name', 'date_created', 'date_updated', 'sales_contact', 'is_prospect')


class CustomerCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Customer
        fields = ('customer_id', 'first_name', 'last_name', 'email', 'phone',
                  'mobile', 'company_name', 'is_prospect', 'sales_contact')
        read_only_fields = ['customer_id', 'sales_contact']


class CustomerCreateSerializerManager(serializers.ModelSerializer):
    def validate(self, data):
        """
        Check the sales_contact is in list of members with sales role
        """
        queryset = Member.objects.filter(role='sales')
        if not data['sales_contact'] in queryset:
            raise serializers.ValidationError(
                {"this sales contact is not recored as a member with sales role"})
        return data

    class Meta:
        model = Customer
        fields = ('customer_id', 'first_name', 'last_name', 'email', 'phone',
                  'mobile', 'company_name', 'is_prospect', 'sales_contact')


class CustomerUpdateSerializerManager(serializers.ModelSerializer):
    sales_contact = serializers.PrimaryKeyRelatedField(
        required=False, queryset=Member.objects.all())

    def validate(self, data):
        """
        Check the sales_contact is in list of members with sales role
        """
        queryset = Member.objects.filter(role='sales')
        if 'sales_contact' in data:
            if not data['sales_contact'] in queryset:
                raise serializers.ValidationError(
                    {"this sales contact is not recored as a member with sales role"})
            return data
        return data

    class Meta:
        model = Customer
        fields = ('customer_id', 'first_name', 'last_name', 'email', 'phone',
                  'mobile', 'company_name', 'date_created', 'date_updated', 'sales_contact', 'is_prospect')
