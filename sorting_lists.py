import operator
import collections

def reverse_sort(iterable_arg):
    """Returns the iterable argument in reverse

    Args:
        iterable_arg (list): A list to be sorted

    Returns:
        list: List sorted in reverse
    """
    return sorted(iterable_arg, reverse = True)

def sort_on_element(list_of_tuples, element=1):
    """Sort a list of tuples based on the second element

    For example, given a list of tuples where each tuple
    contains ('name', age, height), this function will 
    sort and return a list in ascending order of age
    (second element).
    Example 1:
    ___________
    input_list = [('John', 23, 177), ('Ed', 25, 173), ('Al', 21, 168)]
    print(sort_on_element(input_list))
    Output:
    [('Al', 21, 168), ('John', 23, 177), ('Ed', 25, 173)]

    The default behaviour can be modified to use any other
    element if the second argument is provided.
    Example 2:
    ___________
    input_list = [('John', 23, 177), ('Ed', 25, 173), ('Al', 21, 168)]
    print(sort_on_element(input_list, 2))
    Output:
    [('Al', 21, 168), ('Ed', 25, 173), ('John', 23, 177)]

    Args:
        - list_of_tuples (list): A list of tuples
        - element (int, optional): The element number in the tuple on which to sort. Defaults to 1.

    Returns:
        list: List of sorted tuples
"""
    return sorted(list_of_tuples, key=operator.itemgetter(element))

def add_lists(list1, list2):
    """Returns a list by adding the corresponding elements of 2 lists

    Example 1: if lists are equal length, then add all the elements
    _________________________________________________________________
    numbers1 = [1, 2, 3]
    numbers2 = [4, 5, 6]
    print(add_lists(numbers1, numbers2))

    Output:
    [5, 7, 9]

    Example 2: if lists are equal length, then add till length of shorter list
    ____________________________________________________________________________
    numbers1 = [1, 2]
    numbers2 = [4, 5, 6]
    print(add_lists(numbers1, numbers2))

    Output:
    [5, 7]

    Args:
        list1 (list): A list of integers
        list2 (list): A list of integers

    Returns:
        list: List of added values
"""
    return list(map(lambda x, y: x + y, numbers1, numbers2))

def even_odd_sums(iterable):
    """This function that takes a list or tuple of numbers and
    returns a two-element list, containing (respectively) the
    sum of the even-indexed numbers and the sum of the
    odd-indexed numbers.
    So calling the function as `even_odd_sums([10, 20, 30, 40, 50, 60])`,
    you’ll get back `[90, 120]`

    Args:
        iterable (list/tuple of int): An iterable object

    Returns:
        list: two-element list, containing the sum of the even-indexed numbers
        and the sum of the odd-indexed numbers
    """
    return [sum(iterable[0::2]), sum(iterable[1::2])]

def plus_minus(numbers):
    """Takes a list of numbers, and returns the result
    of alternately adding and subtracting them.

    Calling the function as plus_minus([10, 20, 30, 40, 50, 60]),
    you’ll get back the result of 10+20-30+40-50+60, or 50
    """

    if not numbers:
        return 0

    total = numbers.pop(0)

    while numbers:
        total += numbers.pop(0)

        if numbers:
            total -= numbers.pop(0)

    return total

def sort_list_of_dicts(list_of_dicts, *keys_for_sort):
    """Takes a list of dictionaries and sorts it as per the given keys
    Example:
    _________
    Let’s assume you have phone book data in a list of dicts, as follows:

    contact_list = [{'first':'Shashank', 'last':'Chattopadhyaya',
        'email':'mail@shashank.wiki'},
     {'first':'George', 'last':'Lucas',
        'email':'lucasgeorge@starwars.movies'},
     {'first':'Phil', 'last':'Jackson',
        'email':'pjackson@gmail.com'},
     {'first':'Peter', 'last':'Jackson',
        'email':'peter@jackson.movies'}
     ]
    print(sort_list_of_dicts(PEOPLE, 'last', 'first'))

    This should return the list of dicts, but sorted by last name and then by first name.

    Output:
    [{'first': 'Shashank', 'last': 'Chattopadhyaya', 'email': 'mail@shashank.wiki'}, {'first': 'Peter', 'last': 'Jackson', 'email': 'peter@jackson.movies'}, {'first': 'Phil', 'last': 'Jackson', 'email': 'pjackson@gmail.com'}, {'first': 'George', 'last': 'Lucas', 'email': 'lucasgeorge@starwars.movies'}]

    Args:
        list_of_dicts (list of dictionaries): _description_

    Returns:
        list of dictionaries: The sorted list of dictionaries
    """
    return sorted(list_of_dicts, key=operator.itemgetter(*keys_for_sort))

def number_of_vowels(input_string):
    """Returns the number of vowels in a string

    Args:
        input_string (string): a string value

    Returns:
        int: number of vowels in the argument string
    """
    counts = collections.Counter(input_string) # Creates a dict like {'char1': count_of_char1, 'char2': count_of_char2,...}
    vowel_counts = operator.itemgetter('a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U')(counts) # get a list of vowel counts only
    return sum(vowel_counts)

def sort_by_vowel_count(list_of_strings, ascending=True):
    """sort a list of strings according to how many vowels they contain

    Args:
        list_of_strings (list): A list of strings

    Returns:
        list: Argument list sorted as per the number of vowels
    """
    return sorted(list_of_strings, reverse=ascending, key=number_of_vowels)

