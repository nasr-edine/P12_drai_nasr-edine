from rest_framework import serializers
from .models import Member
from django.contrib.auth.hashers import make_password


class MemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = Member
        fields = ('id', 'email', 'password', 'first_name',
                  'last_name', 'phone', 'mobile', 'date_created', 'role')

        # extra_kwargs = {
        #     'password': {'write_only': True},
        # }
