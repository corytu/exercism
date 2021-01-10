from string import ascii_lowercase

def is_pangram(sentence):
    sentence = sentence.lower()
    for letter in ascii_lowercase:
        if letter not in sentence:
            return False
    return True

    # Starred solution: https://exercism.io/tracks/python/exercises/pangram/solutions/66c0c33fd2774c6d9d032b16fae5034d
    # ALPHABET = set(ascii_lowercase)
    # return ALPHABET.issubset(string.lower())
