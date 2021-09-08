
from django.urls import path
from .views import CustomerListView
from .views import CustomerAPIView
from .views import ListCustomer, DetailCustomer

urlpatterns = [

    # with template
    path('withtemplate', CustomerListView.as_view(), name='home'),

    # with api
    path('apiview', CustomerAPIView.as_view()),

    path('<int:pk>/', DetailCustomer.as_view()),
    path('', ListCustomer.as_view()),
]
