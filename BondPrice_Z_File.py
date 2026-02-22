

def getBondPrice_Z(face, couponRate, times, yc):

    c = face * couponRate
    bondPrice = 0

    n = len(times)

    for i, (t, y) in enumerate(zip(times, yc)):

        if i < n - 1:
            cashflow = c
        else:
            cashflow = c + face

        bondPrice += cashflow / (1 + y) ** t


    return bondPrice
