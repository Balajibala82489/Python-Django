
from django.contrib import admin
from django.urls import path, include
from base.views import custom_logout_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('base.urls')),
    path('logout/', custom_logout_view, name='logout'),
]
