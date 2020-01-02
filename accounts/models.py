from django.db import models
from django.db.models import Sum

from django.db.models import F

class TxType(models.IntegerChoices):
    DEPOSIT = 1
    WITHDRAW = 2
    TRANSFER = 3

class Asset(models.Model):
    """
    Description: Model Description
    """
    
    ticker = models.CharField(max_length=10, unique=True)
    unit = models.CharField(max_length=50)

    description = models.TextField()

    class Meta:
        pass

# ID, Ticker, unit, description
DEFAULT_ASSETS = (
    (1, 'BTC', 'satoshi', ''),
    (2, 'ETH', 'wei', ''),
)

class Transaction(models.Model):
    """
    Transaction between accounts
    """
    
    created_at = models.DateTimeField(auto_now=False, auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    asset = models.ForeignKey(Asset, on_delete=models.PROTECT)

    from_account = models.ForeignKey('Account', null=True, default=None, related_name="from_transactions", on_delete=models.PROTECT)
    to_account = models.ForeignKey('Account', null=True, default=None, related_name="to_transactions", on_delete=models.PROTECT)

    # via smallest possible precision
    amount = models.IntegerField()
    from_balance = models.IntegerField(null=True, default=None)
    to_balance = models.IntegerField(null=True, default=None)

    tx_type = models.IntegerField(choices=TxType.choices)

    class Meta:
        pass

class AssetAddress(models.Model):

    created_at = models.DateTimeField(auto_now=False, auto_now_add=True)
    first_used_at = models.DateTimeField(null=True, default=None)
    expired_at = models.DateTimeField(null=True, default=None)

    received = models.IntegerField(default=0)

    asset = models.ForeignKey(Asset, on_delete=models.PROTECT)

    account = models.ForeignKey('Account', null=True, default=None)


# Create your models here.

class Account(models.Model):
    """
    Account which has assets, transactions in and out and balance
    """
    
    created_at = models.DateTimeField(auto_now=False, auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    last_balance = models.IntegerField(default=0)

    asset = models.ForeignKey(Asset, on_delete=models.PROTECT)

    def calculate_total_balance(self):
        return self.from_transactions.aggregate(Sum('amount')) - self.to_transactions.aggregate(Sum('amount'))

    def send_to_account(self, other_account, amount):
        if other_account.asset_id != self.asset_id:
            raise Exception("Mismatching assets")
        if amount <= 0:
            raise Exception("Can't send negative amount")
        if amount > self.last_balance:
            raise Exception("not enough balance")
        sendable_balance = self.calculate_total_balance()
        if amount > sendable_balance:
            raise Exception("not enough balance")

        new_balance = self.last_balance - amount
        rows_updated = Account.objects.filter(id=self.id, last_balance=self.last_balance).update(last_balance=new_balance)
        if rows_updated == 1:
            tx = Transaction.objects.create(from_account=self, to_account=other_account, amount=amount, tx_type=TxType.TRANSFER,
                from_balance=new_balance)
            rows_updated_2 = Account.objects.filter(id=other_account.id).update(last_balance=F('last_balance') + amount)
            if rows_updated_2 < 1:
                # do something, alert adminstrator etc
                pass

        elif rows_updated > 1:
            raise Exception("multiple rows were updated")

    def get_new_address(self):
        address = AssetAddress.objects.filter(asset_id=self.asset_id, account=null).order_by('created_at').first()
        if not address:
            # TODO: request more addresses from daemon ()
            raise Exception("No free addresses")
        return address

    def get_unused_address(self):
        address = AssetAddress.objects.filter(asset_id=self.asset_id, account_id=self.id, first_used_at=None).order_by('created_at').first()
        if not address:
            return self.get_new_address()
        return address

    class Meta:
        pass




