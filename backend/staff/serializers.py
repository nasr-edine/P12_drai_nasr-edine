from rest_framework import serializers
from .models import Member


class MemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = Member
        fields = ('id', 'username', 'first_name', 'last_name', 'email',
                  'phone', 'mobile', 'date_created', 'role')
