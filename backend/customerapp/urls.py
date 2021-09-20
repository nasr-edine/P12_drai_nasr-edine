
from django.urls import path
# from .views import CustomerListView
from .views import CustomerList
from .views import CustomerCreate
from .views import CustomerRetrieve
from .views import CustomerUpdate
from .views import CustomerDestroy


urlpatterns = [

    # with template
    # path('withtemplate/', CustomerListView.as_view(), name='home'),

    # with api
    # path('<int:pk>/', CustomerDetail.as_view()),

    path('', CustomerList.as_view()),
    path('create/', CustomerCreate.as_view()),
    path('get/<int:pk>/', CustomerRetrieve.as_view()),
    path('update/<int:pk>/', CustomerUpdate.as_view()),
    path('destroy/<int:pk>/', CustomerDestroy.as_view()),
]
