def reverse_list(data):
   return data[::-1]
   # """Returns a new list with elements in reverse order."""
  

def get_ends(data):
    return [data[0],data[-1]]
    #"""Returns a new list containing only the first and last elements."""
    

def get_middle(data):

    list_len = len(data)

    if list_len%2 == 0:
        middle_value = int((list_len//2)-1) 
        return data[middle_value]
    else:
        middle_value = int((list_len-1)/2)
        return data[middle_value]

    #"""Returns the middle element. For even lengths, rounds down to the lower index."""

print(get_middle(["a", "b", "c", "d", "e" "f"]))