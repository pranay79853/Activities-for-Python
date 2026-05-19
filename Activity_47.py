def total_calc(total_bill, tip_perc):
    tip_amount = total_bill * (tip_perc / 100)
    total_amount = total_bill + tip_amount
    print(f"Total bill: ${total_bill:.2f}")
    print(f"Tip percentage: {tip_perc}%")
    print(f"Tip amount: ${tip_amount:.2f}")
    print(f"Total amount: ${total_amount:.2f}")
    return total_amount

total_calc(100, 15)