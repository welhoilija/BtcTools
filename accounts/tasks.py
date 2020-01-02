from accounts.models import *
from bitcoinrpc.authproxy import AuthServiceProxy, JSONRPCException
from BtcTools.local_settings import rpc_user, rpc_password

def BTC_refill_address_queue():
    # TODO: move daemon connection string to settings!
    rpc_connection = AuthServiceProxy("http://%s:%s@127.0.0.1:18332"%(rpc_user, rpc_password))

    # try to keep always 1000 address objects ready
    addresses_needed = 1000 - AssetAddress.objects.filter(asset_id=1, account=None).count()

    while i in range(1, addresses_needed):
        address_string = rpc_connection.getnewaddress()
        # TODO: validate address, raise Exception if daemon returrns something that is not excepted


        AssetAddress.objects.create(address=address_string, account=None)

    return rpc_connection.getnewaddress()


def refill_address_queue():
    # fetch new addresses here from the daemon
    BTC_refill_address_queue()


def BTC_check_incoming_transactions():
    # TODO:
    # connect to the BTC daemon
    # get latest transactions with listtransactions, listsinceblock or similar
    rpc_connection = AuthServiceProxy("http://%s:%s@127.0.0.1:18332"%(rpc_user, rpc_password))
    return rpc_connection.listtransactions()
    
    pass

def check_incoming_transactions():
    # fetch new addresses here from the daemon
    BTC_check_incoming_transactions()