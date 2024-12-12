from config import TESTING
from pprint import pprint as print


def get_inputs(prompt: str, type_: type) -> list[float | int]:
    """
    Get a list of inputs from the user and convert them to the specified type (int or float).

    Parameters:
    - prompt: The message to display to the user.
    - type_: The type to convert input values to, either `int` or `float`.

    Returns:
    - A list of user inputs converted to the specified type.
    """
    while True:
        try:
            user_input = input(prompt).strip()
            if not user_input:
                print("Input cannot be empty. Please try again.")
                continue
            if type_ == int:
                return list(map(int, user_input.split()))
            elif type_ == float:
                return list(map(float, user_input.split()))
            else:
                raise TypeError("type_ must be either int or float.")
        except ValueError:
            print("Invalid input. Please try again.")
        except KeyboardInterrupt:
            print("\nExiting program...")
            exit()


def print_if_testing(s: object):
    if TESTING:
        print(s)
