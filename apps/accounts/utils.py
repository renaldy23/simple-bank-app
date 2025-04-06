from core.utils import generate_bank_account_number
from .models import Account

def generate_unique_account_number():
    while True:
        account_number = generate_bank_account_number()
        if not Account.objects.filter(account_number=account_number).exists():
            return account_number
