from django.urls import path

from . import views

urlpatterns = [
    #path('', , name='index'),
    path('<int:Account_id>/', views.AccountViewbyid, name='Accountdetails'),
    path("addresses/<int:Account_id>/", views.AssetAddressViewbyid, name="AssetAddressesbyid"),
    path("addresses/", views.AssetAddressView, name="AssetAddresses")
]