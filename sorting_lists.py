import operator

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


