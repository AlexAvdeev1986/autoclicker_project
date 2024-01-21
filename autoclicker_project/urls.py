# autoclicker_project/urls.py
from django.urls import include, path

urlpatterns = [
    path('autoclicker/', include('autoclicker_app.urls')),
]
