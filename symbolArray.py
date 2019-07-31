def patternCount(text, pattern):
    count = 0
    for i in range(len(text) - len(pattern) + 1):
        if text[i:i + len(pattern)] == pattern:
            count = count + 1
    return count

def symbolArray(genome, symbol):
    array = {}
    n = len(genome)
    extendedGenome = genome + genome[0:n // 2]
    for i in range(n):
        array[i] = patternCount(extendedGenome[i:i + (n // 2)], symbol)
    return array
