def patternMatching(pattern, genome):
    positions = [] # output variable
    # your code here
    for i in range(len(genome) - len(pattern) + 1):
        if genome[i:i + len(pattern)] == pattern:
            positions.append(i)
    return positions
