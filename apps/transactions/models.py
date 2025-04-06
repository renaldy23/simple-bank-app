from django.db import models

from apps.accounts.models import Account
from apps.profiles.models import Profile
from core.models import BaseModel


# Create your models here.
class Transaction(BaseModel):
    user = models.ForeignKey(Profile, on_delete=models.CASCADE, null=True, blank=True)
    from_account = models.ForeignKey(Account, on_delete=models.CASCADE, related_name="from_account")
    to_account = models.ForeignKey(Account, on_delete=models.CASCADE, related_name="to_account")
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    transaction_status = models.CharField(max_length=10, default="pending")
    success_date = models.DateTimeField(null=True, blank=True)
    transaction_description = models.TextField(blank=True, null=True)

    class Meta:
        db_table = "transactions"
