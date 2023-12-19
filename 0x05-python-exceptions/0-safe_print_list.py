#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    """
    prints x elements of a list.

    Args:
        my_list (list): The components to print from the list
        x (int): The amount of my_list items to be printed

    Returns: The number of printed components
    """
    result = 0
    for i in range(x):
        try:
            print("{}".format(my_list[i]), end="")
            result += 1
        except IndexError:
            break
    print("")
    return (result)

