
from django.urls import path
from .views import CustomerListView
from .views import CustomertList, CustomerDetail

urlpatterns = [

    # with template
    path('withtemplate/', CustomerListView.as_view(), name='home'),

    # with api
    path('', CustomertList.as_view()),
    path('<int:pk>/', CustomerDetail.as_view()),
]
