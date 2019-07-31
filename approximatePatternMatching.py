def hammingDistance(p, q):
    count = 0
    for i in range(len(p)):
        if p[i] != q[i]:
            count += 1
    return count

def approximatePatternMatching(text, pattern, d):
    positions = []
    for i in range(len(text) - len(pattern) + 1):
        if hammingDistance(text[i:i + len(pattern)], pattern) <= d:
            positions.append(i)
    return positions
