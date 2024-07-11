from django.urls import path

from medic.apps import MedicConfig
from medic.views import HomeView

app_name = MedicConfig.name

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
]
