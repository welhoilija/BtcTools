from django.shortcuts import render
from django.http import HttpResponse
from accounts.models import Account
from accounts.models import AssetAddress




# Create your views here.
def AccountViewbyid(request, Account_id):
    response = Account.objects.get(id=Account_id)
    address = AssetAddress.objects.filter(account_id=Account_id).order_by('created_at')
    addresslist = []
    for a in address:
        addresslist.append(a.address)

    output = ', '.join([str(response.balance), str(response.asset), str(response.created_at)] + addresslist)

    return HttpResponse(output)


def AssetAddressViewbyid(request, Account_id):
    List = []
    for a in AssetAddress.objects.filter(account_id=Account_id):
        List.append(str(a.address))

    output = ", ".join(List)

    return HttpResponse(output)


def AssetAddressView(request):
    Addresses= AssetAddress.objects.filter(account_id=2)
    List = []
    for a in Addresses:
        List.append(a.address)

    output = ", ".join(List)

    return HttpResponse(output)
