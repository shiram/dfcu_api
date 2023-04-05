from .views import CustomerViewSet, LoanViewSet, AccountViewSet
from django.urls import path

urlpatterns = [
    path('customers/', CustomerViewSet.as_view({'get': 'list'}),  name='customers'),
    path('loans/', LoanViewSet.as_view({'get': 'list'}),  name='loans'),
    path('accounts/', AccountViewSet.as_view({'get': 'list'}),  name='accounts'),
]
