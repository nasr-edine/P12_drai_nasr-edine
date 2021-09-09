from django.views.generic import ListView
from rest_framework import generics
from .models import Customer
from .serializers import CustomerSerializer


# template
class CustomerListView(ListView):
    model = Customer
    template_name = 'customers/customer_list.html'


# api
class CustomertList(generics.ListCreateAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer


class CustomerDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
