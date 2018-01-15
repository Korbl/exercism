def is_pangram(sentence):
    import re
    return len(set(re.sub('[^a-z]', '', sentence.lower()))) == 26
