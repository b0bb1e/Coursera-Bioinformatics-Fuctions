def skewArray(genome):
    skew = [0]
    for i in range(len(genome)):
        if genome[i] == "A" or genome[i] == "T":
            skew.append(skew[i])
        elif genome[i] == "G":
            skew.append(skew[i] + 1)
        elif genome[i] == "C":
            skew.append(skew[i] - 1)
    return skew

def minimumSkew(genome):
    positions = []
    skews = skewArray(genome)
    m = min(skews)
    for i in range(len(skews)):
        if skews[i] == m:
            positions.append(i)
    return positions
