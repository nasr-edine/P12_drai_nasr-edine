from django.contrib import admin
from customerapp.models import Customer
from contractapp.models import Contract
from django.contrib.auth.models import User
from django.utils.translation import ngettext
from django.contrib import messages

from .customfilter import CustomersListFilter


class CustomerAdmin(admin.ModelAdmin):

    list_display = ('customer_id', 'full_name', 'email',
                    'date_created', 'is_prospect', 'contract_count', 'sales_contact')

    fieldsets = (
        ('Personal info', {'fields': ('first_name', 'last_name')}),
        ('Contact', {'fields': ('email', 'phone', 'mobile')}),
        ('company', {'fields': ('company_name',)}),
        ('Change your prospect in customer', {'fields': ('is_prospect',)}),
    )

    ordering = ['-date_created']
    search_fields = ["last_name"]

    list_filter = ['is_prospect', 'date_created', CustomersListFilter]
    date_hierarchy = 'date_created'
    readonly_fields = ('date_created', 'date_updated')
    actions = {'change_prospect_to_customer'}

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

    # displaying  number of contract in list_display
    def contract_count(self, obj):
        return Contract.objects.filter(customer=obj).count()

    # action for change prospect to customer
    def change_prospect_to_customer(self, request, queryset):
        updated = queryset.update(is_prospect=False)
        self.message_user(request, ngettext(
            '%d prospect was successfully marked as customer.',
            '%d prospect were successfully marked as customers.',
            updated,
        ) % updated, messages.SUCCESS)

    # display all customers if the current user has a management role
    # display only the cutomers related to the salesman if the current user have a sales role
    # def get_queryset(self, request):
    #     print('get_queryset')
    #     qs = super().get_queryset(request)
    #     if not qs:
    #         return qs
    #     print(qs)
    #     if request.user.role == 'management' or request.user.role == 'sales':
    #         return qs
    #     if request.user.role == 'support':
    #         qs2 = request.user.events.all()
    #         customers_related_to_event = []
    #         for event in qs2:
    #             print(event.contract.customer.customer_id)
    #             customers_related_to_event.append(
    #                 event.contract.customer.customer_id)
    #         qs = Customer.objects.filter(
    #             customer_id__in=customers_related_to_event)
    #         return qs
    #     print('nothing')
    #     return qs

    # for save automatically the current user in to sales_contact field

    def get_actions(self, request):
        actions = super().get_actions(request)
        if request.user.is_superuser == False or request.user.role != 'management':
            if 'delete_selected' in actions:
                del actions['delete_selected']
        return actions

    def save_model(self, request, obj, form, change):
        obj.sales_contact = request.user
        obj.save()


admin.site.register(Customer, CustomerAdmin)
