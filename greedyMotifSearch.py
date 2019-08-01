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
    
def consensus(motifs):
    countL = count(motifs)
    consensus = ""
    for j in range(len(motifs[0])):
        m = 0
        frequentSymbol = ""
        for symbol in "ACGT":
            if countL[symbol][j] > m:
                m = countL[symbol][j]
                frequentSymbol = symbol
        consensus += frequentSymbol
    return consensus

def hammingDistance(p, q):
    count = 0
    for i in range(len(p)):
        if p[i] != q[i]:
            count += 1
    return count
    
def score(motifs):
    cons = consensus(motifs)
    score = 0
    for motif in motifs:
        score += hammingDistance(motif, cons)
    return score
    
def pr(text, profile):
    p = 1
    # insert your code here
    for i in range(len(text)):
        p *= profile[text[i]][i]
    return p
    
def profileMostProbableKmer(text, k, profile):
    mostP = -1
    mostK = ""
    for i in range(len(text) - k + 1):
        newP = pr(text[i:i + k], profile)
        if newP > mostP:
            mostP = newP
            mostK = text[i:i + k]
    return mostK

def greedyMotifSearch(dna, k, t):
    bestMotifs = []
    for i in range(0, t):
        bestMotifs.append(dna[i][0:k])
    n = len(dna[0])
    for i in range(n - k + 1):
        motifs = []
        motifs.append(dna[0][i:i + k])
        for j in range(1, t):
            p = profile(motifs[0:j])
            motifs.append(profileMostProbableKmer(dna[j], k, p))
        if score(motifs) < score(bestMotifs):
            bestMotifs = motifs
    return bestMotifs
