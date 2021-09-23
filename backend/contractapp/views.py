from rest_framework import generics
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend

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

    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    filterset_fields = ['status', 'sales_contact__email', 'customer__email']
    ordering_fields = ['date_created', 'date_updated']

    def get_queryset(self):
        queryset = Contract.objects.all()
        my_contracts = self.request.query_params.get('my_contracts')
        if my_contracts is not None:
            if my_contracts == 'yes':
                queryset = queryset.filter(sales_contact=self.request.user)
        return queryset

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
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    filterset_fields = ['event_status', 'support_contact__email']
    ordering_fields = ['date_created', 'date_updated']

    def get_queryset(self):
        queryset = Event.objects.all()
        my_events = self.request.query_params.get('my_events')
        if my_events is not None:
            if my_events == 'yes':
                queryset = queryset.filter(support_contact=self.request.user)
        return queryset

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
        if self.request.user.is_superuser or self.request.user.role == 'management':
            return EventUpdateSerializerManager
        else:
            return EventUpdateSerializer


class EventDestroy(generics.DestroyAPIView):
    permission_classes = [IsSuperUserOrManager]
    queryset = Event.objects.all()
    serializer_class = EventSerializer
