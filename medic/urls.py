from django.urls import path

from medic.apps import MedicConfig
from medic.views import HomeView, ContactsView, ProcedureListView, ProcedureDetailView

app_name = MedicConfig.name

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('procedures/', ProcedureListView.as_view(), name='procedure_list'),
    path('procedures/<int:pk>', ProcedureDetailView.as_view(), name='procedure'),

    path('contacts/', ContactsView.as_view(), name='contacts'),
]
