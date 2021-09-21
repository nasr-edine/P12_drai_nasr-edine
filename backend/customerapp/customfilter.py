from django.contrib import admin
from django.utils.translation import gettext_lazy as _


class CustomersListFilter(admin.SimpleListFilter):
    title = _('My customers')

    parameter_name = 'mycustomers'

    def lookups(self, request, model_admin):
        return (
            ('allcustomers', _('All customer registred')),
            ('mycustomers', _('Only my customers')),
        )

    def queryset(self, request, queryset):
        if self.value() == 'allcustomers':
            return queryset
        if self.value() == 'mycustomers':
            return queryset.filter(sales_contact=request.user)


class ContractsListFilter(admin.SimpleListFilter):
    title = _('My contracts')

    parameter_name = 'mycontracts'

    def lookups(self, request, model_admin):
        return (
            ('allcontracts', _('All contracts registred')),
            ('mycontracts', _('Only my contracts')),
        )

    def queryset(self, request, queryset):
        if self.value() == 'allcontracts':
            return queryset
        if self.value() == 'mycontracts':
            return queryset.filter(sales_contact=request.user)


class EventsListFilter(admin.SimpleListFilter):
    title = _('My events')

    parameter_name = 'myevents'

    def lookups(self, request, model_admin):
        return (
            ('allevents', _('All events registred')),
            ('myevents', _('Only my events')),
        )

    def queryset(self, request, queryset):
        if self.value() == 'allevents':
            return queryset
        if self.value() == 'myevents':
            return queryset.filter(support_contact=request.user)
