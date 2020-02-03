from accounts.models import *
from bitcoinrpc.authproxy import AuthServiceProxy, JSONRPCException
from django.conf import settings

def BTC_refill_address_queue():
    # TODO: move daemon connection string to settings!
    daemon_connection = AuthServiceProxy("http://%s:%s@127.0.0.1:18332"%(settings.RPC_USER, settings.RPC_PASSWORD))
    # try to keep always 1000 address objects ready
    addresses_needed = 1000 - AssetAddress.objects.filter(asset_id=1, account=None).count()
    for i in range(1, addresses_needed):
        try:
            address_string = daemon_connection.getnewaddress()
            pass
        except JSONRPCException as e:
            raise Exception("Daemon connection failed")
        
        # TODO: validate address, raise Exception if daemon returrns something that is not excepted
        if 26 <= len(address_string) <= 35:
            AssetAddress.objects.create(address=address_string, account=None, asset_id=1)
        else:
            raise Exception



def refill_address_queue():
    # fetch new addresses here from the daemon
    BTC_refill_address_queue()


def BTC_check_incoming_transactions():
    # TODO:
    # connect to the BTC daemon
    # get latest transactions with listtransactions, listsinceblock or similar
    daemon_connection = AuthServiceProxy("http://%s:%s@127.0.0.1:18332"%(settings.RPC_USER, settings.RPC_PASSWORD))
    recent_transactions = daemon_connection.listtransactions("*", 100)

    # PSEUDOCODE:
    for tx in recent_transactions:
        tx_id = tx["txid"]
        amount = tx["amount"]
        satoshi_amount= int(amount.ToString.replace(".", ""))
        vout = tx["vout"]
        TXidentifier = str(tx_id) + ":" + str(vout)
        txaddress = tx["address"]

        # first look if transaction is already registered & confirmed, if that happens, continue
        # TODO

        # try to look for incoming transaction, if not found create one
        incoming_txs = IncomingTransaction.objects.filter(tx_identifier = TXidentifier)
        asaddress = AssetAddress.objects.get(address=txaddress)
        if incoming_txs.count() < 1:
            inc_tx = IncomingTransaction.objects.create(asset_id=1, address=asaddress, amount=amount, confirmations=tx["confirmations"], tx_identifier=TXidentifier, transaction=None)
        else:
            incoming_tx = incoming_txs.first()

        # and finally, if incoming transaction has enough confirmations credit it to the account
        # TODO 
        if tx["confirmations"]>=2:
            address = AssetAddress.objects.get(address=address)
            accountid = address.account_id
            account = Account.objects.get(id = accountid)
            new_balance = self.last_balance + satoshi_amount
            rows_updated = Account.objects.filter(id = accountid, last_balance=self.last_balance).update(last_balance=new_balance)

            if rows_updated == 1:
                account.update(balance += satoshi_amount)
                account.save()


                



def check_incoming_transactions():
    # fetch new addresses here from the daemon
    BTC_check_incoming_transactions()