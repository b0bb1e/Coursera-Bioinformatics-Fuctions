def complement(pattern):
    complement = ""
    for char in pattern:
        if char == "A":
            complement += "T"
        elif char == "T":
            complement += "A"
        elif char == "G":
            complement += "C"
        elif char == "C":
            complement += "G"
    return complement
