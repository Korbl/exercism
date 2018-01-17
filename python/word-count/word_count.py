def word_count(phrase):
    import re
    import collections
    words = re.findall('[a-z0-9]+\'[a-z0-9]+|[a-z0-9]+', phrase.lower())
    return collections.Counter(words)
