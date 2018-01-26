def hey(phrase):
    words = phrase.split()
    if not words:
        return "Fine. Be that way!"
    elif phrase.isupper():
        return "Whoa, chill out!"
    elif words[-1][-1] == "?":
        return "Sure."
    else:
        return "Whatever."
