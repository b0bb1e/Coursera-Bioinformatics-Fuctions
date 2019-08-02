from random import randint

def randomMotifs(dna, k):
    randomMotifs = []
    for string in dna:
        start = randint(0, len(string) - k)
        randomMotifs.append(string[start: start + k])
    return randomMotifs
