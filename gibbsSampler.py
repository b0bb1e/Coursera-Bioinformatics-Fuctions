from random import randint, uniform

def hammingDistance(p, q):
    count = 0
    for i in range(len(p)):
        if p[i] != q[i]:
            count += 1
    return count

def randomMotifs(dna, k):
    randomMotifs = []
    for string in dna:
        start = randint(0, len(string) - k)
        randomMotifs.append(string[start: start + k])
    return randomMotifs

def pr(text, profile):
    p = 1
    for i in range(len(text)):
        p *= profile[text[i]][i]
    return p

def normalize(probs):
    total = 0
    for key in probs:
        total += probs[key]
    for key in probs:
        probs[key] /= total
    return probs
    
def weightedDie(probs):
    kmer = ""
    r = uniform(0, 1)
    extra = 0
    for key in probs:
        if probs[key] + extra > r:
            kmer = key
            break
        else:
            extra += probs[key]
    return kmer
    
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
    
def profileGeneratedString(text, profile, k):
    probs = {}
    for i in range(0, len(text) - k + 1):
        probs[text[i:i + k]] = pr(text[i:i + k], profile)
    probs = normalize(probs)
    return weightedDie(probs)

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

def gibbsSampler(dna, k, n):
    bestMotifs = randomMotifs(dna, k)
    for i in range(n):
        r = randint(0, len(bestMotifs) - 1)
        newMotifs = []
        for i in range(len(bestMotifs)):
            if i != r:
                newMotifs.append(bestMotifs[i])
        profile = profileWithPseudocounts(newMotifs)
        newMotifs.append(profileGeneratedString(bestMotifs[r], profile, k))
        if score(newMotifs) < score(bestMotifs):
            bestMotifs = newMotifs
    return bestMotifs
