from django.urls import path

from .views import MemberDetail, MembertList

urlpatterns = [
    path('', MembertList.as_view()),
    path('<int:pk>/', MemberDetail.as_view()),
]
