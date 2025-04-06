from django.db import models

from apps.accounts.constant import ACCOUNT_STATUS, ACCOUNT_TYPE
from apps.profiles.models import Profile
from core.models import BaseModel


# Create your models here.
class Account(BaseModel):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    account_number = models.CharField(max_length=100, unique=True)
    identity_number = models.CharField(max_length=100)
    tax_number = models.CharField(max_length=100, blank=True, null=True)
    current_balance = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    currency = models.CharField(max_length=10, default="IDR")
    account_type = models.CharField(max_length=10, choices=ACCOUNT_TYPE, default="starter")
    is_have_limit = models.BooleanField(default=False)
    limit = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    status = models.CharField(max_length=10, choices=ACCOUNT_STATUS, default="active")
    card_holder_name = models.CharField(max_length=255, blank=True, null=True)
    card_name = models.CharField(max_length=100, blank=True, null=True)
    account_purpose = models.CharField(blank=True, null=True)

    class Meta:
        db_table = "accounts"
        indexes = [models.Index(fields=["account_number", "profile"])]
