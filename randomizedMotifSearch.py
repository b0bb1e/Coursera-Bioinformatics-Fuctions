from random import randint

def randomMotifs(dna, k):
    randomMotifs = []
    for string in dna:
        start = randint(0, len(string) - k)
        randomMotifs.append(string[start: start + k])
    return randomMotifs
    
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
    
def pr(text, profile):
    p = 1
    for i in range(len(text)):
        p *= profile[text[i]][i]
    return p

def hammingDistance(p, q):
    count = 0
    for i in range(len(p)):
        if p[i] != q[i]:
            count += 1
    return count

def profileWithPseudocounts(motifs):
    profile = countWithPseudocounts(motifs)
    for lst in profile:
        for i in range(len(profile[lst])):
            profile[lst][i] = profile[lst][i] / (len(motifs) + 4)
    return profile
    
def consensus(motifs):
    countL = countWithPseudocounts(motifs)
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
    
def score(motifs):
    cons = consensus(motifs)
    score = 0
    for motif in motifs:
        score += hammingDistance(motif, cons)
    return score
    
def profileMostProbableKmer(text, k, profile):
    mostP = -1
    mostK = ""
    for i in range(len(text) - k + 1):
        newP = pr(text[i:i + k], profile)
        if newP > mostP:
            mostP = newP
            mostK = text[i:i + k]
    return mostK

def motifs(profile, dna):
    bestMotifs = []
    for string in dna:
        bestMotifs.append(profileMostProbableKmer(string, len(profile["A"]), profile))
    return bestMotifs

def randomizedMotifSearch(dna, k):
    m = randomMotifs(dna, k)
    bestMotifs = m
    while True:
        profile = profileWithPseudocounts(m)
        m = motifs(profile, dna)
        if score(m) < score(bestMotifs):
            bestMotifs = m
        else:
            return bestMotifs 
