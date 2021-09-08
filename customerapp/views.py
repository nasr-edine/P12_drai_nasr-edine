from django.views.generic import ListView
from .models import Customer
from rest_framework import generics
from .models import Customer
from .serializers import CustomerSerializer


class CustomerListView(ListView):
    model = Customer
    template_name = 'customers/customer_list.html'


class CustomerAPIView(generics.ListAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer


class ListCustomer(generics.ListAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer


class DetailCustomer(generics.RetrieveAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
