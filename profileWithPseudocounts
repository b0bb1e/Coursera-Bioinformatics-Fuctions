def countWithPseudocounts(motifs):
    count = {}
    for symbol in "ACGT":
        count[symbol] = []
        for j in range(len(motifs[0])):
             count[symbol].append(0)
    for i in range(len(motifs)):
        for j in range(len(motifs[0])):
            symbol = motifs[i][j]
            count[symbol][j] += 1
    for lttr in count:
        for i in range(len(count[lttr])):
            count[lttr][i] += 1
    return count

def profileWithPseudocounts(motifs):
    profile = countWithPseudocounts(motifs)
    for lst in profile:
        for i in range(len(profile[lst])):
            profile[lst][i] = profile[lst][i] / (len(motifs) + 4)
    return profile
