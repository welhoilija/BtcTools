from django.db import models
from accounts.models import Account
from django.db.models import Sum

# Create your models here.



class Loan(models.Model):

    """
    Lending model

    """


    created_at = models.DateTimeField(auto_now=False, auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=False, auto_now_add=True)

    collateral_account = models.ForeignKey(Account, on_delete=models.PROTECT)

    pay_date = models.DateTimeField("pay date")

    amount = models.CharField(max_length=50)

    interest_rate = models.DecimalField(max_digits=10, decimal_places=9)

    def calculate_collateral(self, amount, interest_rate, pay_date):
        return self.amount + (self.amount * self.interest_rate)*((self.pay_date - self.created_at)/30)


    
    email = models.EmailField(max_length=254)

    def __str__(self):
        return self.amount + " " + self.email

    class Meta:
        pass

