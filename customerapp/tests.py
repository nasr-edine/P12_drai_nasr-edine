from django.test import TestCase

from customerapp.models import Customer

# Create your tests here.


class CustomerModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        Customer.objects.create(
            first_name='first customer', last_name='a body here')

    def test_name_content(self):
        customer = Customer.objects.get(customer_id=1)
        expected_object_name = f'{customer.first_name}'
        self.assertEquals(expected_object_name, 'first customer')
