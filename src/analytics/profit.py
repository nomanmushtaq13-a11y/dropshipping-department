def calculate(cost,sell):
    cost=float(cost)
    sell=float(sell)

    if sell<=0:
        return 0

    return round(((sell-cost)/sell)*100,2)
