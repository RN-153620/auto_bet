from decimal import Decimal


def generate(base_amount):
    base_amount = base_amount
    if base_amount >= 1:
        return [base_amount, base_amount + Decimal("1"), base_amount + Decimal("2")]
    else:
        return [base_amount, base_amount + Decimal("0.1"), base_amount + Decimal("0.2")]


def remove_both_ends(sequence):
    sequence.pop(-1)
    sequence.pop(0)
    if len(sequence) >= 2:
        sequence.pop(0)
        sequence.pop(-1)
    return sequence

def add_num(sequence):
    first_num = sequence[0]
    end_num = sequence[-1]
    sequence.append(first_num + end_num)
    return sequence



