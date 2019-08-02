def pr(text, profile):
    p = 1
    for i in range(len(text)):
        p *= profile[text[i]][i]
    return p
