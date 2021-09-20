from django.views.generic import ListView
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from staff.permissions import IsManagerOrSalesman

from .models import Contract
from .serializers import ContractSerializer
from .serializers import ContractCreateSerializer
from .serializers import ContractCreateSerializerManager
from .models import Event
from .serializers import EventSerializer


class ContractListView(ListView):
    model = Contract
    template_name = 'contracts/contract_list.html'


class ContracttList(generics.ListCreateAPIView):
    queryset = Contract.objects.all()
    serializer_class = ContractSerializer


class ContractDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Contract.objects.all()
    serializer_class = ContractSerializer


class ContracttList(generics.ListAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Contract.objects.all()
    serializer_class = ContractSerializer


class ContractCreate(generics.CreateAPIView):
    permission_classes = [IsAuthenticated, IsManagerOrSalesman]
    queryset = Contract.objects.all()
    # serializer_class = CustomerCreateSerializer

    def get_serializer_class(self):
        if self.request.user.role == 'sales':
            return ContractCreateSerializer
        if self.request.user.is_superuser == True or self.request.user.role == 'management':
            return ContractCreateSerializerManager

    def perform_create(self, serializer):
        if self.request.user.role == 'sales':
            serializer.save(sales_contact=self.request.user)
        if self.request.user.is_superuser == True or self.request.user.role == 'management':
            serializer.save()


class EventList(generics.ListCreateAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer


class EventDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
