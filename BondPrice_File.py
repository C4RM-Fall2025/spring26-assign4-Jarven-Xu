
def getBondPrice(y, face, couponRate, m, ppy=1):
    
    if ppy == 1:

        r = y
        c = face * couponRate
        n = m

        x = 0

        for t in range(1, n + 1):
            x += c / (1 + r) ** t

        x += face / (1 + r) ** n

    elif ppy == 2:

        r = y / 2
        c = face * couponRate / 2
        n = m * 2

        x = 0

        for t in range(1, n + 1):
            x += c / (1 + r) ** t

        x += face / (1 + r) ** n


    return x
