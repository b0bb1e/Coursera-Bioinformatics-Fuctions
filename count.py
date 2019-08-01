def count(motifs):
    count = {}
    for symbol in "ACGT":
        count[symbol] = []
        for j in range(len(motifs[0])):
             count[symbol].append(0)
    for i in range(len(motifs)):
        for j in range(len(motifs[0])):
            symbol = motifs[i][j]
            count[symbol][j] += 1
    return count
