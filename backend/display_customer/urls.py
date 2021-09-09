from django.urls import path
from .views import DisplayCustomerList
from .views import DisplayContractList

urlpatterns = [
    path('customers/', DisplayCustomerList),
    path('contracts/', DisplayContractList),
]
