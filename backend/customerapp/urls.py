
from django.urls import path

# from .views import CustomerUpdate
from .views import CustomerDestroy, CustomerDetail, CustomerList

urlpatterns = [
    path('', CustomerList.as_view()),
    path('<int:pk>/', CustomerDetail.as_view()),
    path('destroy/<int:pk>/', CustomerDestroy.as_view()),
]
