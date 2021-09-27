from django.contrib.auth.models import Group, Permission

from staff.models import Member

sales_group = Group.objects.create(name='sales')
support_group = Group.objects.create(name='support')
mgmt_group = Group.objects.create(name='management')

can_view_user = Permission.objects.get(name='Can view user')
can_add_user = Permission.objects.get(name='Can add user')
can_change_user = Permission.objects.get(name='Can change user')
can_delete_user = Permission.objects.get(name='Can delete user')

can_view_customer = Permission.objects.get(name='Can view customer')
can_add_customer = Permission.objects.get(name='Can add customer')
can_change_customer = Permission.objects.get(name='Can change customer')
can_delete_customer = Permission.objects.get(name='Can delete customer')

can_view_contract = Permission.objects.get(name='Can view contract')
can_add_contract = Permission.objects.get(name='Can add contract')
can_change_contract = Permission.objects.get(name='Can change contract')
can_delete_contract = Permission.objects.get(name='Can delete contract')

can_view_event = Permission.objects.get(name='Can view event')
can_add_event = Permission.objects.get(name='Can add event')
can_change_event = Permission.objects.get(name='Can change event')
can_delete_event = Permission.objects.get(name='Can delete event')

mgmt_group.permissions.add(can_view_user, can_add_user, can_change_user, can_delete_user,
                           can_view_customer, can_add_customer, can_change_customer, can_delete_customer,
                           can_view_contract, can_add_contract, can_change_contract, can_delete_contract,
                           can_view_event, can_add_event, can_change_event, can_delete_event)

sales_group.permissions.add(can_view_customer, can_add_customer, can_view_contract,
                            can_add_contract, can_view_event, can_add_event)

support_group.permissions.add(can_view_customer, can_view_contract, can_view_event, can_change_event)

members = Member.objects.all()

for member in members:
    member.role = 'management'
    member.save()
    print(member)
