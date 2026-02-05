def multiplication_table():
    """Returns a list of products for a 12x12 table (1x1, 1x2... 12x12)."""
    table = []
    for i in range(1,13):
        for j in range(1,13):
            table.append(i*j)
    return table


def get_multiples_of_three(numbers):
    """Uses a list comprehension to return numbers > 0 and divisible by 3."""
    return [num for num in numbers if num>0 and num%3==0]


def merge_lists(list1, list2):
    """Uses zip to merge two lists into a list of tuples."""
    return list(zip(list1 , list2))