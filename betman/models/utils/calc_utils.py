"""Valuation of Calculation Methods"""
from decimal import Decimal

def get_betting_amount(sequence):
    a = sequence[0]
    b = sequence[-1]
    return a + b

def select_chip(amount):
    FIVE_HUNDRED = Decimal("500")
    ONE_HUNDRED = Decimal("100")
    TWENTY_FIVE = Decimal("25")
    FIVE = Decimal("5")
    TWO = Decimal("2")
    ONE = Decimal("1")
    ZERO_FIVE = Decimal("0.5")
    ZERO_TWO = Decimal("0.2")
    ZERO_ONE = Decimal("0.1")

    if amount.compare(FIVE_HUNDRED) >= 0:
        return FIVE_HUNDRED
    
    if amount.compare(ONE_HUNDRED) >= 0:
        return ONE_HUNDRED
    
    if amount.compare(TWENTY_FIVE) >= 0:
        return TWENTY_FIVE
    
    if amount.compare(FIVE) >= 0:
        return FIVE
    
    if amount.compare(TWO) >= 0:
        return TWO
    
    if amount.compare(ONE) >= 0:
        return ONE
    
    if amount.compare(ZERO_FIVE) >= 0:
        return ZERO_FIVE
    
    if amount.compare(ZERO_TWO) >= 0:
        return ZERO_TWO
    
    else:
        return ZERO_ONE