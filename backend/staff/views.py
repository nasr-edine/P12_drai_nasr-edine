from django.contrib.auth.models import Group
from rest_framework import generics

from .models import Member
from .permissions import IsSuperUserOrManager
from .serializers import MemberSerializer
from .serializers import MemberUpdateSerializer


class MembertList(generics.ListCreateAPIView):
    permission_classes = [IsSuperUserOrManager]

    queryset = Member.objects.all()
    serializer_class = MemberSerializer

    def perform_create(self, serializer):

        sales_group = Group.objects.get(name='sales')
        support_group = Group.objects.get(name='support')
        mgmt_group = Group.objects.get(name='management')

        instance = serializer.save()
        instance.set_password(instance.password)
        if instance.role == 'sales':
            instance.groups.add(sales_group)
        elif instance.role == 'support':
            instance.groups.add(support_group)
        elif instance.role == 'management':
            instance.groups.add(mgmt_group)
        instance.save()


class MemberDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsSuperUserOrManager]
    queryset = Member.objects.all()
    serializer_class = MemberUpdateSerializer
