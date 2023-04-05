from django.shortcuts import render
from rest_framework.permissions import IsAuthenticated
from django.views.decorators.csrf import csrf_exempt
from .models import Customer, Loan, Account
from .serializers import Customerserializer, LoanSerializer, AccountSerializer
from rest_framework import permissions, viewsets


# Create your views here.
class CustomerViewSet(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = Customerserializer
    permission_classes = (permissions.IsAuthenticated, )

class LoanViewSet(viewsets.ModelViewSet):
    queryset = Loan.objects.all()
    serializer_class = LoanSerializer
    permission_classes = (permissions.IsAuthenticated, )

class AccountViewSet(viewsets.ModelViewSet):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer
    permission_classes = (permissions.IsAuthenticated, )
