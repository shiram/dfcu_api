from .views import CustomerViewSet, LoanViewSet, AccountViewSet, CustomerLoansView, home, logout_user
from django.urls import path

urlpatterns = [
    path('', home,  name='home'),
    path('logout', logout_user,  name='logout'),
    path('customers/', CustomerViewSet.as_view({'get': 'list'}),  name='customers'),
    path('loans/', LoanViewSet.as_view({'get': 'list'}),  name='loans'),
    path('accounts/', AccountViewSet.as_view({'get': 'list'}),  name='accounts'),
    path('accounts/loans/', CustomerLoansView.as_view(), name='customer-loans'),
]
