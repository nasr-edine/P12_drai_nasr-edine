from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters, generics, status
from rest_framework.response import Response

from staff.permissions import (IsManagerOrSalesContact, IsManagerOrSalesman,
                               IsManagerOrSupportContact,
                               IsManagerOrSupportMan, IsSuperUserOrManager)

from .models import Contract, Event
from .serializers import (ContractCreateByManagerSerializer,
                          ContractSerializer, ContractUpdateSerializer,
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

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        print(instance)
        print(instance.event_status)
        if instance.event_status == "finished" and self.request.user.role == 'support':
            return Response({'message': "Yon can change this event because it is finished"},
                            status=status.HTTP_403_FORBIDDEN)
        serializer = self.get_serializer(instance, data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data)

    def get_serializer_class(self):
        if self.request.user.is_superuser or self.request.user.role == 'management':
            return EventUpdateSerializerManager
        else:
            return EventUpdateSerializer


class EventDestroy(generics.DestroyAPIView):
    permission_classes = [IsSuperUserOrManager]
    queryset = Event.objects.all()
    serializer_class = EventSerializer
