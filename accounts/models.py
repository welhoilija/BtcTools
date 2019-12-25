from django.db import models
from django.db.models import Sum

class TxType(models.IntegerChoices):
    DEPOSIT = 1
    WITHDRAW = 2
    TRANSFER = 3

class Transaction(models.Model):
    """
    Transaction between accounts
    """
    
    created_at = models.DateTimeField(auto_now=False, auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=False, auto_now_add=True)

    from_account = models.ForeignKey('Account', null=True, default=None, related_name="from_transactions")
    to_account = models.ForeignKey('Account', null=True, default=None, related_name="to_transactions")

    # via smallest possible precision
    amount = models.IntegerField()
    balance = models.IntegerField()

    tx_type = models.IntegerField(choices=TxType.choices)

    class Meta:
        pass

# Create your models here.

class Account(models.Model):
    """
    Account which has assets, transactions in and out and balance
    """
    
    created_at = models.DateTimeField(auto_now=False, auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=False, auto_now_add=True)

    last_balance = models.IntegerField(default=0)

    def calculate_total_balance(self):
        return self.from_transactions.aggregate(Sum('amount')) - self.to_transactions.aggregate(Sum('amount'))

    def send_to_account(self, other_account, amount):
        if amount <= 0:
            raise Exception("can't send negative amount")
        if amount > self.last_balance:
            raise Exception("not enough balance")
        sendable_balance = self.calculate_total_balance()
        if amount > sendable_balance:
            raise Exception("not enough balance")

        new_balance = self.last_balance - amount
        rows_updated = Account.objects.filter(id=self.id, last_balance=self.last_balance).update(last_balance=new_balance)
        if rows_updated == 1:
            tx = Transaction.objects.create(from_account=self, to_account=other_account, amount=amount, balance=new_balance, tx_type=TxType.TRANSFER)
        elif rows_updated > 1:
            raise Exception("multiple rows were updated")

    class Meta:
        pass
