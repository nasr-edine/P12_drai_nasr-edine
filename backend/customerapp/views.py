from django.views.generic import ListView
from rest_framework import generics
from .models import Customer
from .serializers import CustomerSerializer
from .serializers import CustomerCreateSerializer
from .serializers import CustomerUpdateSerializerManager
from .serializers import CustomerCreateSerializerManager

from rest_framework.permissions import IsAuthenticated

from staff.permissions import IsManagerOrSalesman
from staff.permissions import IsManagerOrSalesContact
from staff.permissions import IsSuperUserOrManager

# template
# class CustomerListView(ListView):
#     model = Customer
#     template_name = 'customers/customer_list.html'


# api
# class CustomertList(generics.ListCreateAPIView):
#     queryset = Customer.objects.all()
#     serializer_class = CustomerSerializer


# class CustomerRetrieveUpdate(generics.RetrieveUpdateAPIView):
#     queryset = Customer.objects.all()
#     serializer_class = CustomerSerializer


class CustomerDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

################################################################


class CustomerList(generics.ListAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer


class CustomerCreate(generics.CreateAPIView):
    permission_classes = [IsAuthenticated, IsManagerOrSalesman]
    queryset = Customer.objects.all()
    # serializer_class = CustomerCreateSerializer

    def get_serializer_class(self):
        if self.request.user.role == 'sales':
            return CustomerCreateSerializer
        if self.request.user.is_superuser == True or self.request.user.role == 'management':
            return CustomerCreateSerializerManager

    def perform_create(self, serializer):
        if self.request.user.role == 'sales':
            serializer.save(sales_contact=self.request.user)
        if self.request.user.is_superuser == True or self.request.user.role == 'management':
            serializer.save()


class CustomerRetrieve(generics.RetrieveAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer


class CustomerUpdate(generics.UpdateAPIView):
    permission_classes = [IsAuthenticated, IsManagerOrSalesContact]
    queryset = Customer.objects.all()
    # serializer_class = CustomerUpdateSerializerManager

    def get_serializer_class(self):
        if self.request.user.role == 'sales':
            return CustomerCreateSerializer
        if self.request.user.is_superuser == True or self.request.user.role == 'management':
            return CustomerUpdateSerializerManager

    def perform_create(self, serializer):
        if self.request.user.role == 'sales':
            serializer.save(sales_contact=self.request.user)
        if self.request.user.is_superuser == True or self.request.user.role == 'management':
            serializer.save()


class CustomerDestroy(generics.DestroyAPIView):
    permission_classes = [IsAuthenticated, IsSuperUserOrManager]
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
