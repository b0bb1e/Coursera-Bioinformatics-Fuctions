from random import uniform

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
