def normalize(probs):
    total = 0
    for key in probs:
        total += probs[key]
    for key in probs:
        probs[key] /= total
    return probs
