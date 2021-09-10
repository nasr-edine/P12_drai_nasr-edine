
from django.urls import path
from .views import MembertList, MemberDetail

urlpatterns = [
    path('', MembertList.as_view()),
    path('<int:pk>/', MemberDetail.as_view()),
]
