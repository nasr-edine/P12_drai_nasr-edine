from django.test import TestCase

from customerapp.models import Customer
from contractapp.models import Contract
# Create your tests here.


class CustomerModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Create a customer
        testcustomer1 = Customer.objects.create(
            first_name='john', last_name='doo')
        testcustomer1.save()

        # Create a contract for this customer
        test_contract = Contract.objects.create(
            customer=testcustomer1, status=True, amount=9.99)
        test_contract.save()

    def test_contract_content(self):
        customer = Customer.objects.get(customer_id=1)
        expected_object_name = f'{customer.first_name} {customer.last_name}'
        self.assertEquals(expected_object_name, 'john doo')

        contract = Contract.objects.get(contract_id=1)
        customer = f'{contract.customer}'
        status = contract.status
        amount = contract.amount

        self.assertEqual(customer, 'john doo')
        self.assertEqual(status, True)
        self.assertEqual(amount, 9.99)
