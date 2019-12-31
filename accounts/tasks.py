from accounts.models import *

def BTC_refill_address_queue():
    # TODO:
    # connect to the BTC daemon
    # get addresses via json-rpc command
    # create address object¨
    pass


def refill_address_queue():
    # fetch new addresses here from the daemon
    BTC_refill_address_queue()


def BTC_check_incoming_transactions():
    # TODO:
    # connect to the BTC daemon
    # get latest transactions with listtransactions, listsinceblock or similar
    pass

def check_incoming_transactions():
    # fetch new addresses here from the daemon
    BTC_check_incoming_transactions()