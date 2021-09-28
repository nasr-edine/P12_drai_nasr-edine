
from django.urls import path

from .views import (ContractDestroy, ContractDetail, ContractList,
                    EventDestroy, EventDetail, EventList)

urlpatterns = [
    path('', ContractList.as_view()),
    path('<int:pk>/', ContractDetail.as_view()),
    path('destroy/<int:pk>/', ContractDestroy.as_view()),

    path('event/', EventList.as_view()),
    path('event/<int:pk>/', EventDetail.as_view()),
    path('event/destroy/<int:pk>/', EventDestroy.as_view()),
]
