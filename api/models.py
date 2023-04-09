from django.db import models
from django.utils.translation import gettext_lazy as _


# A customer model to store customer details.
class Customer(models.Model):
	first_name = models.CharField(max_length=50)
	last_name = models.CharField(max_length=50)
	email = models.EmailField(max_length=100)
	phone = models.CharField(max_length=15)
	address = models.CharField(max_length=50)
	customer_id = models.CharField(max_length=256)
	created_at = models.DateTimeField(auto_now_add=True)

	class Meta:
		verbose_name = _("Customer")
		verbose_name_plural = _("Customers")

	def __str__(self):
		return (f"{self.first_name} {self.last_name}")
	
class Loan(models.Model):
	LOAN_STATUS = (
		('CLD', 'Closed'),
		('ACT', 'Active'),
		('PD', 'Pending Distbursement')
	)
	loan_id = models.CharField(max_length=256)
	customer_id = models.ForeignKey(Customer, related_name="customer_loan", null=True, on_delete=models.SET_NULL)
	loan_status = models.CharField(max_length=50, choices = LOAN_STATUS)
	disbursment_date = models.DateTimeField()
	outstanding_amount = models.IntegerField()
	created_at = models.DateTimeField(auto_now_add=True)

	class Meta:
		verbose_name = _("Loan")
		verbose_name_plural = _("Loans")

	def __str__(self):
		return (f"{self.loan_id} - {self.customer_id}")


class Account(models.Model):
	account_id = models.CharField(max_length=256)
	customer_id = models.ForeignKey(Customer, related_name="customer_account", null=True, on_delete=models.SET_NULL)
	account_number = models.CharField(max_length=15)
	created_at = models.DateTimeField(auto_now_add=True)

	class Meta:
		verbose_name = _("Account")
		verbose_name_plural = _("Accounts")

	def __str__(self):
		return (f"{self.customer_id} - {self.account_number}")

# add requests log model

class APILog(models.Model):
	class Meta:
		verbose_name = _("API Log")
		verbose_name_plural = _("API Logs")

	log_id = models.CharField(max_length=5)
	num_requests = models.IntegerField(default=0)
	num_failed_requests = models.IntegerField(default=0)
	num_pos_requests = models.IntegerField(default=0)
	num_neg_requests = models.IntegerField(default=0)

	def __str__(self) -> str:
		return f"{self.log_id}"