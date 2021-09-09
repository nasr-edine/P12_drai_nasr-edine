from django.views.generic import ListView
from rest_framework import generics

from .models import Contract
from .serializers import ContractSerializer

from .models import Event
from .serializers import EventSerializer


class ContractListView(ListView):
    model = Contract
    template_name = 'contracts/contract_list.html'


# class ContractAPIView(generics.ListAPIView):
#     queryset = Contract.objects.all()
#     serializer_class = ContractSerializer


# class ListContract(generics.ListAPIView):
#     queryset = Contract.objects.all()
#     serializer_class = ContractSerializer


# class DetailContract(generics.RetrieveAPIView):
#     queryset = Contract.objects.all()
#     serializer_class = ContractSerializer


class ContracttList(generics.ListCreateAPIView):
    queryset = Contract.objects.all()
    serializer_class = ContractSerializer


class ContractDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Contract.objects.all()
    serializer_class = ContractSerializer


class EventList(generics.ListCreateAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer


class EventDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
