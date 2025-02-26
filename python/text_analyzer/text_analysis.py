def word_count(string: str):
    '''Returns the amount of words in a provided string'''
    return len(string.split(" "))

def unique_words(string: str):
    '''Returns the amount of unique words in a provided string'''
    return len(set(string.split(" ")))