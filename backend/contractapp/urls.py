
from django.urls import path
from .views import ContractListView
# from .views import ContractAPIView
# from .views import ListContract, DetailContract
from .views import ContracttList, ContractDetail, ContractCreate, ContractRetrieve, ContractDestroy, ContractUpdate
from .views import EventList, EventRetrieve, EventDestroy

urlpatterns = [

    # with template
    path('contractwithtemplate/', ContractListView.as_view()),

    # with api
    # path('apiview', ContractAPIView.as_view()),

    # path('<int:pk>/', DetailContract.as_view()),
    # path('', ListContract.as_view()),


    path('', ContracttList.as_view()),
    path('<int:pk>/', ContractDetail.as_view()),

    path('create/', ContractCreate.as_view()),
    path('get/<int:pk>/', ContractRetrieve.as_view()),
    path('update/<int:pk>/', ContractUpdate.as_view()),
    path('destroy/<int:pk>/', ContractDestroy.as_view()),

    # path('event/', EventList.as_view()),
    # path('event/<int:pk>/', EventDetail.as_view()),

    path('event/', EventList.as_view()),
    path('event/get/<int:pk>/', EventRetrieve.as_view()),
    path('event/destroy/<int:pk>/', EventDestroy.as_view()),

]
