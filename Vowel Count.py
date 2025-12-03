def get_count(sentence):
    return sum([sentence.count(c) for c in "aeiou"])
