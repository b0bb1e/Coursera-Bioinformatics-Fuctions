def patternCount(text, pattern):
  count = 0
  for i in range(len(text) - len(pattern) + 1):
    if text[i:i + len(pattern)] == pattern:
        count = count + 1
  return count

def fasterSymbolArray(genome, symbol):
    array = {}
    n = len(genome)
    extendedGenome = genome + genome[0:n // 2]

    array[0] = patternCount(genome[0:n // 2], symbol)

    for i in range(1, n):
        array[i] = array[i - 1]

        if extendedGenome[i - 1] == symbol:
            array[i] = array[i] - 1
        if extendedGenome[i + (n // 2) - 1] == symbol:
            array[i] = array[i] + 1
    return array
