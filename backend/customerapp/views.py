from rest_framework import generics
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend

from staff.permissions import (IsManagerOrSalesContact, IsManagerOrSalesman,
                               IsSuperUserOrManager)

from .models import Customer
from .serializers import (CustomerCreateSerializerBySalesMan,
                          CustomerSerializer, CustomerUpdateSerializerManager)


class CustomerList(generics.ListCreateAPIView):
    permission_classes = [IsManagerOrSalesman]
    queryset = Customer.objects.all()

    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    filterset_fields = ['is_prospect', 'sales_contact__email', 'date_created']
    ordering_fields = ['date_updated', 'last_name']

    def get_queryset(self):
        queryset = Customer.objects.all()
        my_customers = self.request.query_params.get('my_customers')
        if my_customers is not None:
            if my_customers == 'yes':
                queryset = queryset.filter(sales_contact=self.request.user)
        return queryset

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

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return CustomerSerializer
        if self.request.user.role == 'sales':
            print('sales condition')
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
