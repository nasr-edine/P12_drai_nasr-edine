import requests

from django.shortcuts import render

# Create your views here.


def DisplayCustomerList(request):
    response = requests.get('http://127.0.0.1:8000/customer/')
    customers = response.json()
    print(customers)
    return render(request, 'customers/customers_list.html', {
        'customers': customers
    })


def DisplayContractList(request):
    response = requests.get('http://127.0.0.1:8000/contract/')
    contracts = response.json()
    print(contracts)
    return render(request, 'contracts/contracts_list.html', {
        'contracts': contracts
    })
