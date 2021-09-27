from django.contrib import admin
from django.contrib.auth.models import Group

from staff.models import Member


class MemberAdmin(admin.ModelAdmin):
    list_display = ('id', 'full_name', 'email',
                    'role')
    fieldsets = (
        ('Personal info', {'fields': ('first_name', 'last_name')}),
        ('Contact', {'fields': ('email', 'phone', 'mobile')}),
        ('security', {'fields': ('username', 'password')}),
        ('Permissions', {'fields': ('role',)}),
    )
    radio_fields = {'role': admin.HORIZONTAL}
    ordering = ['-date_created']
    list_filter = ['role']
    readonly_fields = ('date_created', 'password')

    def save_model(self, request, obj, form, change):
        obj.is_staff = True
        obj.set_password(obj.password)
        mgmt_group = Group.objects.get(name='management')
        sales_group = Group.objects.get(name='sales')
        support_group = Group.objects.get(name='support')
        no_privilege = Group.objects.get(name='no_privilege')

        obj.save()
        if obj.role == 'sales':
            obj.groups.add(sales_group)
        elif obj.role == 'support':
            obj.groups.add(support_group)
        elif obj.role == 'management':
            obj.groups.add(mgmt_group)
        else:
            obj.groups.add(no_privilege)


admin.site.register(Member, MemberAdmin)
