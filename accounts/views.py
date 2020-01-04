from django.shortcuts import render
from django.http import HttpResponse
from accounts.models import Account
from accounts.models import AssetAddress




# Create your views here.
def AccountViewbyid(request, Account_id):
    response = Account.objects.get(id=Account_id)
    output = ', '.join([str(response.balance), str(response.asset), str(response.created_at)])



    return HttpResponse(output)



def AssetAddressView(request):
    List = AssetAddress.objects.all()
    output = ", ".join([a.address for a in List])
    
    


    return HttpResponse(output)
