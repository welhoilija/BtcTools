from accounts.models import *
from bitcoinrpc.authproxy import AuthServiceProxy, JSONRPCException
from django.conf import settings

def BTC_refill_address_queue():
    # TODO: move daemon connection string to settings!
    rpc_connection = AuthServiceProxy("http://%s:%s@127.0.0.1:18332"%(settings.RPC_USER, settings.RPC_PASSWORD))
    # try to keep always 1000 address objects ready
    addresses_needed = 1000 - AssetAddress.objects.filter(asset_id=1, account=None).count()
    for i in range(1, addresses_needed):
        address_string = rpc_connection.getnewaddress()
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
    rpc_connection = AuthServiceProxy("http://%s:%s@127.0.0.1:18332"%(rpc_user, rpc_password))
    recent_transactions = rpc_connection.listtransactions()

    # PSEUDOCODE:
    for tx in recent_transactions:
        tx_id = tx["txid"]
        amount = amount

        # first look if transaction is already registered & confirmed, if that happens, continue
        # TODO

        # try to look for incoming transaction, if not found create one
        incoming_txs = IncomingTransaction.objects.filter(blaa)
        if incoming_txs.count() < 0:
            inc_tx = IncomingTransaction.objects.create(blaa)
        else:
            incoming_tx = incoming_txs.first()

        # and finally, if incoming transaction has enough confirmations credit it to the account
        # TODO 

def check_incoming_transactions():
    # fetch new addresses here from the daemon
    BTC_check_incoming_transactions()