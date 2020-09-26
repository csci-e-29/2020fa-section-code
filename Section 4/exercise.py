# this file is the exercise with the answers redacted
from functools import reduce


def is_float(input_value):
    """
    :param input_value: of some unknown type
    :return: true if type is float
    """

    # TODO: given a list of values, return a list of the ones that are floats



def filter_floats_from_list(input_list):
    """
    :param input_list: a list of arbitrary values
    :return: list of floats
    """

    # TODO: use filter with a named function

    # TODO: rewrite named function as lambda function


def list_odds_in_range(range_int):
    """
    :param range_int: int
    :return: list
    """
    # create a list of odd numbers
    odds = []
    for i in range(range_int):
        if i % 2:
            odds.append(i)
    return odds

    # TODO: rewrite in functional style
    # return list(a for a in range(n) if a % 2)


def sum_using_reduce(odd_list):
    # TODO: return sum of list items using reduce
    return


if __name__ == '__main__':
    """
    What is a package?
    
    "A module in python is simply a way to organize the code, and it contains either python classes or just functions. 
    If you need those classes or functions in your project, you just import them. For instance, the math module in 
    python contains just a bunch of functions, and you just call those needed (math.sin)."
    - t.ly/lWZv
    
    """

    # TODO: import SectionFour and call greet function to greet some friends

    # use filter to return floats from a list
    print(filter_floats_from_list([1, 2, 3, 'a', 'b', 'c', 3.42, 2.11, 13.5]))

    # get a list of the odd numbers in a range
    print(list_odds_in_range(100))

    # sum odd elements in range using reduce
    print(sum_using_reduce(list_odds_in_range(10)))
