from rest_framework import generics

from staff.permissions import (IsManagerOrSalesContact, IsManagerOrSalesman,
                               IsManagerOrSupportContact,
                               IsManagerOrSupportMan, IsSuperUserOrManager)

from .models import Contract, Event
from .serializers import (ContractSerializer, ContractUpdateSerializer,
                          ContractCreateByManagerSerializer,
                          EventCreateByManagerSerializer, EventSerializer,
                          EventUpdateSerializer, EventUpdateSerializerManager)


class ContractList(generics.ListCreateAPIView):
    permission_classes = [IsManagerOrSalesman]
    queryset = Contract.objects.all()

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return ContractSerializer
        if self.request.user.role == 'sales':
            return ContractSerializer
        if self.request.user.is_superuser or self.request.user.role == 'management':
            return ContractCreateByManagerSerializer

    def perform_create(self, serializer):
        if self.request.user.role == 'sales':
            serializer.save(sales_contact=self.request.user)
        if self.request.user.is_superuser or self.request.user.role == 'management':
            serializer.save()


class ContractDetail(generics.RetrieveUpdateAPIView):
    permission_classes = [IsManagerOrSalesman, IsManagerOrSalesContact]
    queryset = Contract.objects.all()
    serializer_class = ContractUpdateSerializer


class ContractDestroy(generics.DestroyAPIView):
    permission_classes = [IsSuperUserOrManager]
    queryset = Contract.objects.all()
    serializer_class = ContractSerializer


class EventList(generics.ListCreateAPIView):
    permission_classes = [IsManagerOrSalesman]
    queryset = Event.objects.all()
    serializer_class = EventSerializer

    def get_serializer_class(self):
        if self.request.user.is_superuser or self.request.user.role == 'management':
            return EventCreateByManagerSerializer
        else:
            return EventSerializer


class EventDetail(generics.RetrieveUpdateAPIView):
    permission_classes = [IsManagerOrSupportMan, IsManagerOrSupportContact]
    queryset = Event.objects.all()
    serializer_class = EventSerializer

    def get_serializer_class(self):
        if self.request.user.role == 'support':
            return EventUpdateSerializer
        if self.request.user.is_superuser or self.request.user.role == 'management':
            return EventUpdateSerializerManager


class EventDestroy(generics.DestroyAPIView):
    permission_classes = [IsSuperUserOrManager]
    queryset = Event.objects.all()
    serializer_class = EventSerializer
