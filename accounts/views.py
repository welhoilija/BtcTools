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



def AssetAddressView(request):
    List = AssetAddress.objects.get(account=True)
    output = ", ".join([str(a.address) , str(a.Account_id)])
    
    


    return HttpResponse(output)
