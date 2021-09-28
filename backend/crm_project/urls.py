from django.contrib import admin
from django.urls import path, include  # new
from rest_framework_simplejwt.views import (
    TokenObtainPairView, TokenRefreshView)

# django admin header customization
admin.site.site_header = 'CRM Event   interface'
admin.site.index_title = "Welcome to the Event CRM"

urlpatterns = [
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    path('adminzone/', admin.site.urls),
    path('customer/', include('customerapp.urls')),
    path('contract/', include('contractapp.urls')),
    path('member/', include('staff.urls')),
]
