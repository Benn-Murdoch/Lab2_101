def get_evens(n):
    # """Returns a list of even integers from 0 up to and including n."""
    num_list = range (n+1)
    evens = [] 
    for num in num_list: 
        if num % 2 == 0: 
            evens.append(num)
    return evens
print(get_evens(10))



def find_second_largest(numbers):
    #"""Returns the second largest number by iterating through the list twice."""
    maxes = [] 
   
    while len(maxes) < 2:
        cur_max = numbers[0]

        for max in numbers: 
            if max > cur_max:
                cur_max = max
        while cur_max in numbers:
            numbers.remove(cur_max)

        maxes.append(cur_max)
    print(maxes)
    return maxes[1]



    

def count_vowels(text):
    # """Returns the total number of vowels (a, e, i, o, u) in a string."""
    word_list = text.lower()
    vowels = "aeiou"
    total_vowels = 0

    for letter in word_list: 
        if letter in vowels: 
            total_vowels += 1

    return total_vowels

