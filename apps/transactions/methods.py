import time
from datetime import datetime

from apps.transactions.models import Transaction


def update_transaction_process(transaction_id):
    try:
        transaction = Transaction.objects.get(id=transaction_id)
        from_account = transaction.from_account
        to_account = transaction.to_account
        amount = transaction.amount

        if transaction.transaction_status == 'pending' :
            from_account.current_balance -= amount
            to_account.current_balance += amount
            from_account.save()
            time.sleep(1)
            to_account.save()
            time.sleep(1)

            transaction.transaction_status = 'completed'
            transaction.success_date = datetime.now()
            transaction.save()

    except Exception as e:
        transaction = Transaction.objects.get(id=transaction_id)
        transaction.transaction_status = 'failed'
        transaction.save()