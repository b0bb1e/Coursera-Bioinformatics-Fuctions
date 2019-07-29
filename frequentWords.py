def patternCount(text, pattern):
    count = 0
    for i in range(len(text) - len(pattern) + 1):
        if text[i:i + len(pattern)] == pattern:
            count = count + 1
    return count

def frequencyMap(text, k):
    freq = {}
    n = len(text)
    for i in range(n-k+1):
        pattern = text[i:i+k]
        freq[pattern] = patternCount(text, pattern)
    return freq

def frequentWords(Text, k):
    words = []
    freq = frequencyMap(Text, k)
    m = max(freq.values())
    for key in freq:
        if freq[key] == m: words.append(key)
    return words
