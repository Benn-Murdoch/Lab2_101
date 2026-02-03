def map_word_lengths(words):
    """
    Given a list of strings, returns a dictionary where:
    - Key: The string (word)
    - Value: The length of that string
    """
    Word_lengths_dict={}
    for word in words: 
        Word_lengths_dict[word] = len(word)
    return Word_lengths_dict

