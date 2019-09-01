'''
Letisia Tatimoa Pangata'a
COMPSCI 280 - Lab 05 
Student ID : 995182480

- Taken from Lab 02.

'''

def factorial(first, second): 
    return first % second

def add(first, second, conv=2): # Task 2.2 Added an optional parameter to add.
    return first + second

def fibonacci(length):
    def internal(first, second, count):
        third = add(first, second) # Adds the first and second integer.
        count -= 1 # The counter.
        if count == 0: # If the count has reached to 0, return the last amount.
            return third # Return the third value.
        else:
            return internal(third, second, count)

    return internal(0, 1, length)

HEX_CHARS = {
    10: 'A',
    11: 'B',
    12: 'C',
    13: 'D',
    14: 'E',
    15: 'F'
}

def convert_base(num, n):
    """Change a base 10 number to a base-n number. Supports up to base 16. """
    new_num_string = ''
    current = num
    while current != 0:
        remainder = current % n
        if remainder > 9:
            remainder_string = HEX_CHARS[remainder]
        elif remainder >= 36:
            remainder_string = '('+str(remainder)+')'
        else:
            remainder_string = str(remainder)
        new_num_string = remainder_string+new_num_string
        current = current//n
    return new_num_string
.py
=======
def factorial(first, second): 
    return first % second


def add(first, second, conv=2): # Task 2.2 Added an optional parameter to add.
    return first + second

def fibonacci(length):
    def internal(first, second, count):
        third = add(first, second) # Adds the first and second integer.
        count -= 1 # The counter.
        if count == 0: # If the count has reached to 0, return the last amount.
            return third # Return the third value.
        else:
            return internal(third, second, count)

    return internal(0, 1, length)

HEX_CHARS = {
    10: 'A',
    11: 'B',
    12: 'C',
    13: 'D',
    14: 'E',
    15: 'F'
}

def convert_base(num, n):
    """Change a base 10 number to a base-n number. Supports up to base 16. """
    new_num_string = ''
    current = num
    while current != 0:
        remainder = current % n
        if remainder > 9:
            remainder_string = HEX_CHARS[remainder]
        elif remainder >= 36:
            remainder_string = '('+str(remainder)+')'
        else:
            remainder_string = str(remainder)
        new_num_string = remainder_string+new_num_string
        current = current//n
    return new_num_string
