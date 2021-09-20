from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from django.contrib.auth.models import Group

from .models import Member
from .serializers import MemberSerializer

from .permissions import IsSuperUserOrManager

# class RegisterAPI(generics.CreateAPIView):
#     """
#     Create a new user.
#     """
#     serializer_class = Member

#     def post(self, request, *args, **kwargs):
#         serializer = self.get_serializer(data=request.data)
#         if not serializer.is_valid():q
#             return Response(serializer.errors, status=status.HTTP_409_CONFLICT
#                             )
#         member = serializer.save()

#         return Response({
#             "user": MemberSerializer(member, context=self.get_serializer_context()).data,
#             "message": "User Created Successfully. Now perform Login to get your token"},
#             status=status.HTTP_201_CREATED)


class MembertList(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated, IsSuperUserOrManager]

    queryset = Member.objects.all()
    serializer_class = MemberSerializer

    def get_queryset(self):
        print('hello')
        return super().get_queryset()
    # for hashing password

    def perform_create(self, serializer):
        print('perform_create called')
        instance = serializer.save()
        print(instance)
        sales_group = Group.objects.get(name='sales')
        support_group = Group.objects.get(name='support')
        mgmt_group = Group.objects.get(name='management')
        instance.set_password(instance.password)
        if instance.role == 'sales':
            print(f'{instance} is attach to group sales')
            instance.groups.add(sales_group)
        elif instance.role == 'support':
            print(f'{instance} is attach to group support')
            instance.groups.add(support_group)
        elif instance.role == 'management':
            print(f'{instance} is attach to group management')
            instance.groups.add(mgmt_group)
        instance.save()


class MemberDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated, IsSuperUserOrManager]
    queryset = Member.objects.all()
    serializer_class = MemberSerializer
