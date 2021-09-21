from rest_framework import generics

from .models import Customer

from .serializers import CustomerSerializer
from .serializers import CustomerCreateSerializerBySalesMan
from .serializers import CustomerUpdateSerializerManager


from staff.permissions import IsManagerOrSalesman
from staff.permissions import IsManagerOrSalesContact
from staff.permissions import IsSuperUserOrManager


class CustomerList(generics.ListCreateAPIView):
    permission_classes = [IsManagerOrSalesman]
    queryset = Customer.objects.all()

    def get_serializer_class(self):
        if self.request.user.role == 'sales':
            return CustomerCreateSerializerBySalesMan
        else:
            return CustomerSerializer

    def perform_create(self, serializer):
        if self.request.user.role == 'sales':
            serializer.save(sales_contact=self.request.user)
        if self.request.user.is_superuser or self.request.user.role == 'management':
            serializer.save()


class CustomerDetail(generics.RetrieveUpdateAPIView):
    permission_classes = [IsManagerOrSalesContact]
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return CustomerSerializer
        if self.request.user.role == 'sales':
            return CustomerCreateSerializerBySalesMan
        if self.request.user.is_superuser or self.request.user.role == 'management':
            return CustomerUpdateSerializerManager

    def perform_create(self, serializer):
        if self.request.user.role == 'sales':
            serializer.save(sales_contact=self.request.user)
        if self.request.user.is_superuser or self.request.user.role == 'management':
            serializer.save()


class CustomerDestroy(generics.DestroyAPIView):
    permission_classes = [IsSuperUserOrManager]
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
