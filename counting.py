import collections

def count_characters(input_string: str):
    """Returns a dictionary with the number of occurrences of a particular character

Example:
_______________

print(count_characters('abcdab'))

Output:
{'a':2, 'b':2, 'c':1, 'd':1}

Args:
    input_string (str): A normal string
"""
    return collections.Counter(input_string)


