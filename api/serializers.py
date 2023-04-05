from rest_framework import serializers

from .models import Customer, Loan, Account

class Customerserializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = "__all__"

class LoanSerializer(serializers.ModelSerializer):
    class Meta:
        model = Loan
        fields = "__all__"

class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = "__all__"