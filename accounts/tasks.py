from accounts.models import *
from bitcoinrpc.authproxy import AuthServiceProxy, JSONRPCException
from BtcTools.local_settings import rpc_user, rpc_password

def BTC_refill_address_queue():
    # TODO:
    # connect to the BTC daemon
    # get addresses via json-rpc command
    # create address object¨
    rpc_connection = AuthServiceProxy("http://%s:%s@127.0.0.1:18332"%(rpc_user, rpc_password))
    return rpc_connection.getnewaddress()


    pass


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