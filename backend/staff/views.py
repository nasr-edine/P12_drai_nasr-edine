from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from .models import Member
from .serializers import MemberSerializer


# class RegisterAPI(generics.CreateAPIView):
#     """
#     Create a new user.
#     """
#     serializer_class = Member

#     def post(self, request, *args, **kwargs):
#         serializer = self.get_serializer(data=request.data)
#         if not serializer.is_valid():
#             return Response(serializer.errors, status=status.HTTP_409_CONFLICT
#                             )
#         member = serializer.save()

#         return Response({
#             "user": MemberSerializer(member, context=self.get_serializer_context()).data,
#             "message": "User Created Successfully. Now perform Login to get your token"},
#             status=status.HTTP_201_CREATED)


class MembertList(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Member.objects.all()
    serializer_class = MemberSerializer

    # for hashing password
    def perform_create(self, serializer):
        instance = serializer.save()
        instance.set_password(instance.password)
        instance.save()


class MemberDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Member.objects.all()
    serializer_class = MemberSerializer
