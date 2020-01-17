import re

def is_isogram(string):
    processed_string = re.sub(r"[\s-]", "", string).lower()
    return len(set(processed_string)) == len(processed_string)
