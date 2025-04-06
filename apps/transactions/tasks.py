from huey.contrib.djhuey import task

from apps.transactions.methods import update_transaction_process


@task()
def create_transaction_async(transaction_id):
    print(f"Triggered transaction for ID: {transaction_id}")
    update_transaction_process(transaction_id)