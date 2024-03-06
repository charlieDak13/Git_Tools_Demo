"""
By: Charlie Dakai
THis is a demo explainnig how to use git command line tools
December 2023
"""

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.


def print_goodbye(name):
    print('Goodbye!')





def collect_even_numbers(stop):
    """
    this function displays all even numbers to the "stop" parameter, non inclusive
    """
    even_numbers = []
    for number in range(stop):
        if number % 2 == 0:
            even_numbers.append(number)
    return even_numbers


def another_function():
    print('This is another function')


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
