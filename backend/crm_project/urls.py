from django.contrib import admin
from django.urls import path, include  # new

urlpatterns = [
    path('admin/', admin.site.urls),
    path('customer/', include('customerapp.urls')),  # new
    path('contract/', include('contractapp.urls')),
    path('member/', include('staff.urls')),
]
