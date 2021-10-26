from django.db import models, transaction
from django.utils.translation import gettext_lazy as _
from accounts.models import CustomUser

import uuid

class Wallet(models.Model):
    uid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.OneToOneField(CustomUser, on_delete=models.SET_NULL, null=True)
    balance = models.DecimalField(_("balance"), max_digits=100, decimal_places=2)
    account_name = models.CharField(_("account name"), max_length=250)
    account_number = models.CharField(_("account number"), max_length=100)
    bank = models.CharField(_("bank"), max_length=100)
    phone_number = models.CharField(_("phone number"), max_length=15)
    password = models.CharField(_("password"), max_length=200)
    created = models.DateTimeField(auto_now_add=True)
    

""""
class WalletTransaction(models.Model):
    transaction_id = models.CharField()
    status = models.Choices()
    pass
"""
