from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView
from .models import Customer


class CustomerListView(ListView):
    model = Customer
    template_name = 'customers/customer_list.html'
