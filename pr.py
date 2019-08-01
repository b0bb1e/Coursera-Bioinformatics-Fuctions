def pr(text, profile):
    p = 1
    # insert your code here
    for i in range(len(text)):
        p *= profile[text[i]][i]
    return p
