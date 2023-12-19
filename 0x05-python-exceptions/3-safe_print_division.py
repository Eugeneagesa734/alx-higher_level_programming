#!/usr/bin/python3
def safe_print_division(a, b):
    """
    Prints the result of dividing a by b.
    If b is 0 or not a number, prints an error message.
    """
    if isinstance(a, (int, float)) and isinstance(b, (int, float)) and b != 0:
        result = a / b
        print("Inside result: {}".format(result))
        return result
    else:
        print("Error: Cannot divide {} by {}".format(a, b))
        return None

