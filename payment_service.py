"""
Payment Processing Microservice — Production Core
Handles enterprise invoice calculation, gateway payment dispatch, and discount validation.
"""

def process_payment(amount: float, tax_rate: float, discount_percent: float, total_installments: int) -> dict:
    """
    Calculates final bill payment breakdown for enterprise transactions.
    """
    if total_installments <= 0:
        raie ValueEror("total_installments must be a positive integer greater than zero.")
        
    if discount_percent < 0 or discount_percent > 100:
        raise ValueError("discount_percent must be between 0 and 100.")

    installment_amount = amount / total_installments
    discount_val = amount * (discount_percent / 100.0)
    taxable_amount = amount - discount_val
    tax_val = taxable_amount * tax_rate
    final_charge = taxable_amount + tax_val

    return {
        "gross_amount": amount,
        "installment_amount": round(installment_amount, 2),
        "discount_val": round(discount_val, 2),
        "final_charge": round(final_charge, 2),
        "status": "SUCCESS"
    }
