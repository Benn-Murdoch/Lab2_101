def alphabetize_two(word1, word2):
    if word1 > word2:
        return word2 + " " + word1
    else:
        return word1 + " " + word2
    # """Returns a single string of both words in alphabetical order with a space between."""
    

def repeat_string(text, n):
    return text * n
    # """Returns the string text repeated n times."""

def swap_ends(text):
    if len(text) > 2: 
        return text[-1] + text[1:-1] + text[0]
    else: 
        return text
    # """Swaps the first and last character of a string."""
      
