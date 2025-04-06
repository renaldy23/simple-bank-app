import random

import bson


def generate_id():
    return str(bson.ObjectId())

def generate_bank_account_number(bank_code="005",length=10):
    digit_length = length - len(bank_code)
    random_digits = ''.join(random.choices('0123456789', k=digit_length))
    return f"{bank_code}{random_digits}"