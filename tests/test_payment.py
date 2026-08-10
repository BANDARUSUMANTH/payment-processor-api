import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import pytest
from payment_service import process_payment

def test_process_payment_valid():
    res = process_payment(amount=1000.0, tax_rate=0.18, discount_percent=10.0, total_installments=4)
    assert res["gross_amount"] == 1000.0
    assert res["installment_amount"] == 250.0
    assert res["discount_val"] == 100.0
    assert res["final_charge"] == 1062.0
    assert res["status"] == "SUCCESS"

def test_process_payment_zero_installments():
    with pytest.raises(ValueError):
        process_payment(amount=500.0, tax_rate=0.18, discount_percent=10.0, total_installments=0)

def test_process_payment_invalid_discount():
    with pytest.raises(ValueError):
        process_payment(amount=500.0, tax_rate=0.18, discount_percent=150.0, total_installments=2)
