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
