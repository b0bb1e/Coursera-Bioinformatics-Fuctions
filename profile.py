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
    
def profile(motifs):
    profile = count(motifs)
    for lst in profile:
        for i in range(len(profile[lst])):
            profile[lst][i] = round(profile[lst][i] / len(motifs), 1)
    return profile
