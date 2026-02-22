
def getBondDuration(y, face, couponRate, m, ppy = 1):

    r = y
    c = face * couponRate
    n = m

    bondPrice = 0
    weightedPV = 0

    for t in range(1, n + 1):

        pv = c / (1 + r) ** t

        bondPrice += pv
        weightedPV += t * pv


    pvFace = face / (1 + r) ** n

    bondPrice += pvFace
    weightedPV += n * pvFace


    bondDuration = weightedPV / bondPrice

    return bondDuration
