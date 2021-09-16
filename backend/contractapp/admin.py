from django.contrib import admin
from .models import Contract
from customerapp.models import Customer
from .models import Event
from customerapp.customfilter import ContractsListFilter
from customerapp.customfilter import EventsListFilter
# Register your models here.


@admin.register(Contract)
class ContractAdmin(admin.ModelAdmin):
    list_display = ('contract_id', 'customer', 'status',
                    'amount', 'payment_due', 'event_count', 'sales_contact')

    fields = ('customer', 'status', 'amount', 'payment_due')
    ordering = ['-date_created']
    search_fields = ("customer__last_name", )
    list_filter = [ContractsListFilter, 'status']
    date_hierarchy = 'date_created'
    readonly_fields = ('date_created', 'date_updated')

    # Either member with sales role can update  his own customers
    # Or member with management role can change any customers
    def has_change_permission(self, request, obj=None):
        if request.user.role == 'sales':
            if obj is not None:
                if obj.sales_contact == request.user:
                    return True
                else:
                    return False
            return True
        elif request.user.role == 'management':
            return True
        else:
            return False

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.role == 'management' or request.user.role == 'sales':
            return qs
        if request.user.role == 'support':
            qs2 = request.user.events.all()
            contracts_related_to_event = []
            for event in qs2:
                print(event.contract.contract_id)
                contracts_related_to_event.append(
                    event.contract.contract_id)
            qs = Contract.objects.filter(
                contract_id__in=contracts_related_to_event)
            return qs

    # filtering foreignkey field for displaying only my own customers with customer status (not prospect)

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        print(db_field)
        if db_field.name == "customer":
            kwargs["queryset"] = Customer.objects.filter(
                is_prospect=False, sales_contact=request.user)
        return super().formfield_for_foreignkey(db_field, request, **kwargs)

    def get_actions(self, request):
        actions = super().get_actions(request)
        if request.user.is_superuser == False or request.user.role != 'management':
            if 'delete_selected' in actions:
                del actions['delete_selected']
        return actions
    # for display event number

    def event_count(self, obj):
        return Event.objects.filter(contract=obj).count()

    def save_model(self, request, obj, form, change):
        obj.sales_contact = request.user
        obj.save()


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    '''Admin View for Event'''
    list_display = ('event_id', 'contract', 'event_status',
                    'event_date', 'support_contact')

    fieldsets = (
        ('Contract related', {'fields': ('contract',)}),
        ('Date', {'fields': ('event_date',)}),
        ('Details', {'fields': ('event_status', 'attendees', 'notes')}),
        ('Contact', {'fields': ('support_contact',)}),
    )
    ordering = ['-date_created']
    search_fields = ("contract__customer__last_name", )
    list_filter = ['event_date', 'event_status', EventsListFilter]
    date_hierarchy = 'date_created'
    readonly_fields = ('date_created', 'date_updated')

    def has_change_permission(self, request, obj=None):
        if request.user.role == 'support':
            if obj is not None:
                if obj.support_contact == request.user:
                    return True
                else:
                    return False
            return True
        elif request.user.role == 'management':
            return True
        else:
            return False

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.role == 'management' or request.user.role == 'sales':
            return qs
        if request.user.role == 'support':
            return qs.filter(support_contact=request.user)

    # def has_delete_permission(self, request, obj=None):
    #     if request.user.role == 'sales':
    #         if obj is not None:
    #             if obj.contract.sales_contact == request.user:
    #                 return True
    #             else:
    #                 return False
    #         return True
    #     elif request.user.role == 'management':
    #         return True
    #     else:
    #         return False

# admin.site.register(Contract, ContractAdmin)
# admin.site.register(Event, EventAdmin)
