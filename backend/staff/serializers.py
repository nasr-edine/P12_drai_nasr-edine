from rest_framework import serializers

from .models import Member


class MemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = Member
        fields = ('id', 'username', 'email', 'password', 'first_name',
                  'last_name', 'phone', 'mobile', 'date_created', 'role', 'is_staff', 'is_superuser')

        extra_kwargs = {
            'password': {'write_only': True},
        }


class MemberUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Member
        fields = ('id', 'username', 'email', 'first_name',
                  'last_name', 'phone', 'mobile', 'date_created', 'role', 'is_staff', 'is_superuser')
