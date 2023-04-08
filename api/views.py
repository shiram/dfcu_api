from django.shortcuts import render
from .models import Customer, Loan, Account
from .serializers import Customerserializer, LoanSerializer, AccountSerializer
from rest_framework import permissions, viewsets
from django.http import JsonResponse, HttpResponse
from rest_framework.views import APIView
import json



class CustomerViewSet(viewsets.ModelViewSet):
	"""
	customer view
	"""
	queryset = Customer.objects.all()
	serializer_class = Customerserializer
	permission_classes = (permissions.IsAuthenticated, )

class LoanViewSet(viewsets.ModelViewSet):
	"""
	loan view
	"""
	queryset = Loan.objects.all()
	serializer_class = LoanSerializer
	permission_classes = (permissions.IsAuthenticated, )

class AccountViewSet(viewsets.ModelViewSet):
	"""
	account view
	"""
	queryset = Account.objects.all()
	serializer_class = AccountSerializer
	permission_classes = (permissions.IsAuthenticated, )

class CustomerLoansView(APIView):
	"""
	view customer's loans
	"""
	permission_classes = (permissions.IsAuthenticated, )

	def post(self, request):
		data = json.loads(request.body.decode("utf-8"))
		if data['account']:
			account = data['account']
			try:
				customer_account = Account.objects.get(account_number=account)
				if customer_account:
					account_number = customer_account.account_number
					customer_id = customer_account.customer_id.customer_id
					customer_name = f"{customer_account.customer_id.first_name} {customer_account.customer_id.last_name}" 
					customer_loans = Loan.objects.filter(customer_id = customer_account.customer_id.id)
					if customer_loans:
						loans = []
						for loan in customer_loans:
							loan_dict = {
								'loan_id': loan.loan_id,
								'disbursement_date': loan.disbursment_date,
								'outstanding_amount': loan.outstanding_amount
							}
							loans.append(loan_dict)
						return JsonResponse({'response': {
							'customer_id': customer_id, 
							'customer_name': customer_name,
							'customer_account': account_number, 
							'customer_loans': loans
							}})
					else:
						message = 'No Loans found for account - '+account
						return JsonResponse({'response': message})
				else:
					message = 'The Account number ('+account+') provided does not exist.'
					return JsonResponse({'response': message})
			except Exception as e:
				message = 'An error ocurred. The Account number ('+account+') provided does not exist.'
				print("Error Here")
				print(e)
				return JsonResponse({'response': message})
		else:
			return JsonResponse({'response': 'You need to provide account number.'})
