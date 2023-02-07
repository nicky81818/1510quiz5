"""
Nicole Hsu A01340726
"""


def is_sorted(number_list):
    """
    Check if number_list is sorted.

    This function returns True if number_list is sorted in non-decreasing order, otherwise False. Non-decreasing order
    means that each integer in the list is equal to or greater than the preceding integer.

    :param number_list: a list of integer numbers
    :precondition: number_list must be a list of integer numbers
    :postcondition: correctly asserts True that number_list is sorted, else False
    :return: True if number_list is sorted, else False, as a boolean
    >>> is_sorted([0, 1, 2, 3])
    True
    >>> is_sorted([3, 2, 0, 1])
    False
    """
    sorted_list = sorted(number_list)
    return sorted_list == number_list


def main():
    """
    Drives the program.
    """


if __name__ == "__main__":
    main()
