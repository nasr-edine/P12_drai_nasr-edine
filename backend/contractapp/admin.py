
from django.contrib import admin

from customerapp.customfilter import ContractsListFilter, EventsListFilter
from customerapp.models import Customer
from staff.models import Member

from .models import Contract, Event

# Register your models here.


@admin.register(Contract)
class ContractAdmin(admin.ModelAdmin):
    list_display = ('contract_id', 'customer', 'status',
                    'amount', 'payment_due', 'event_count', 'sales_contact')
    # list_display_links = ('customer',)
    fields = ('customer', 'status', 'amount', 'payment_due')
    ordering = ['-date_created']
    search_fields = ("customer__last_name", )
    list_filter = [ContractsListFilter, 'status']
    date_hierarchy = 'date_created'
    readonly_fields = ('date_created', 'date_updated')

    def get_readonly_fields(self, request, obj=None):
        if obj:  # editing an existing object
            return self.readonly_fields + ('customer',)
        return self.readonly_fields

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

    # filtering foreignkey field for displaying only my own customers with customer status (not prospect)

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        print(db_field)
        if request.user.role == 'sales':
            if db_field.name == "customer":
                kwargs["queryset"] = Customer.objects.filter(
                    is_prospect=False, sales_contact=request.user)
        if request.user.role == 'management':
            if db_field.name == "customer":
                kwargs["queryset"] = Customer.objects.filter(
                    is_prospect=False)
        return super().formfield_for_foreignkey(db_field, request, **kwargs)

    def get_actions(self, request):
        actions = super().get_actions(request)
        if not request.user.is_superuser or request.user.role != 'management':
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
    # list_display_links = ('contract',)
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

    def get_readonly_fields(self, request, obj=None):
        if obj and request.user.role == 'support':
            return self.readonly_fields + ('contract', 'support_contact',)
        if obj:  # editing an existing object
            return self.readonly_fields + ('contract',)
        return self.readonly_fields

    def has_change_permission(self, request, obj=None):
        if request.user.role == 'support':
            if obj is not None:
                if obj.support_contact == request.user and obj.event_status == 'progress':
                    return True
                else:
                    return False
            return True
        elif request.user.role == 'management':
            return True
        else:
            return False

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        print(db_field)
        if request.user.role == 'sales':
            # Customize foreygn key contract in addform for only display contract has signed
            if db_field.name == "contract":
                kwargs["queryset"] = Contract.objects.filter(
                    status=True, sales_contact=request.user, event__isnull=True)
            print(db_field.name)
        if request.user.role == 'management':
            if db_field.name == "contract":
                kwargs["queryset"] = Contract.objects.filter(
                    status=True, event__isnull=True)

        # Customize foreygn key support_contact in addform for only display members with support role
        if db_field.name == "support_contact":
            print(db_field.name)
            kwargs["queryset"] = Member.objects.filter(role='support', )
        return super().formfield_for_foreignkey(db_field, request, **kwargs)

# admin.site.register(Contract, ContractAdmin)
# admin.site.register(Event, EventAdmin)
