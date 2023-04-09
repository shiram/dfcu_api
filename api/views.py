from django.shortcuts import render, redirect
from .models import Customer, Loan, Account, APILog
from .serializers import Customerserializer, LoanSerializer, AccountSerializer
from rest_framework import permissions, viewsets
from django.http import JsonResponse
from rest_framework.views import APIView
import json
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

def home(request):
	log = APILog.objects.filter(log_id = "LG01X")
	response = {}
	for i in log:
		response['num_requests'] = i.num_requests
		response['num_failed_requests'] = i.num_failed_requests
		response['num_pos_requests'] = i.num_pos_requests
		response['num_neg_requests'] = i.num_neg_requests

	# check to see if user logging in
	if request.method == 'POST':
		username = request.POST['username']
		password = request.POST['password']

		#authenticate user
		user = authenticate(request, username=username, password=password)

		#check user exists
		if user is not None:
			login(request, user)
			messages.success(request, "You have successfully logged in.")
			return redirect('home')
		else:
			messages.success(request, "There was an error logging in.")
			return redirect('home')
	else:
		return render(request, 'home.html', {'log': response})

def logout_user(request):
	logout(request)
	messages.success(request, "You have been logged out...")
	return redirect('home')

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

	def requestLog(self, action):
		log = APILog.objects.get(log_id = "LG01X")
		print(log)
		if log:
			log.num_requests += 1
			if action == 1:
				log.num_failed_requests += 1
			elif action == 2:
				log.num_pos_requests += 1
			elif action == 3:
				log.num_neg_requests += 1
			log.save()
		else:
			if action == 1:

				num_failed_requests = 1
				num_pos_requests = 0
				num_neg_requests = 0

			elif action == 2:

				num_pos_requests = 1
				num_failed_requests = 0
				num_neg_requests = 0

			elif action == 3:

				num_neg_requests = 1
				num_pos_requests = 0
				num_failed_requests = 0

			APILog(
				log_id="LG01X", 
				num_requests = 1, 
	  			num_failed_requests = num_failed_requests,
				num_pos_requests = num_pos_requests,
				num_neg_requests = num_neg_requests
				).save()


	def post(self, request):
		if 'account' in request.POST and request.POST['account']:
			data = request.POST['account']
		else:
			data = request.data['account']
		if data:
			try:
				customer_account = Account.objects.get(account_number=data)
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
						# log the request
						self.requestLog(action=2)

						return JsonResponse({'response': {
							'customer_id': customer_id, 
							'customer_name': customer_name,
							'customer_account': account_number, 
							'customer_loans': loans
							}})
					else:
						# log the request
						self.requestLog(action=3)

						message = 'No Loans found for account - ' + data
						return JsonResponse({'response': message})
				else:
					# log the request
					self.requestLog(action=1)

					message = 'The Account number (' + data + ') provided does not exist.'
					return JsonResponse({'response': message})
			except Exception as e:
				# log the request
				self.requestLog(action=1)

				message = 'An error ocurred. The Account number (' + data + ') provided does not exist.'
				return JsonResponse({'response': message})
		else:
			return JsonResponse({'response': 'You need to provide account number.'})
