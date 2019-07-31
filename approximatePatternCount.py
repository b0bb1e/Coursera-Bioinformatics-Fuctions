def hammingDistance(p, q):
    count = 0
    for i in range(len(p)):
        if p[i] != q[i]:
            count += 1
    return count

def approximatePatternCount(pattern, text, d):
    count = 0
    for i in range(len(text) - len(pattern) + 1):
        if hammingDistance(text[i:i + len(pattern)], pattern) <= d:
            count += 1
    return count
