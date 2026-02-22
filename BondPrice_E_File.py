def getBondPrice_E(face, couponRate, m, yc):
    c = face * couponRate
    bondPrice = 0
    for t, y in enumerate(yc, start = 1):
        if t < m:
            cashflow = c
        else:
            cashflow = c + face
        bondPrice += cashflow / (1 + y) ** t
    return bondPrice

