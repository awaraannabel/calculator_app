# Constants
FILE_NAME = 'equation.txt'
ZERO_DIVISION_ERROR_MSG = "Cannot divide by zero"
VALUE_ERROR_MSG = 'Oops! Must input an integer'

def get_user_input():
    """Get input from the user."""
    num_one = int(input('Enter first number: '))
    operator = input('Enter operator: ')
    num_two = int(input('Enter second number: '))
    return num_one, operator, num_two

def perform_calculation(num_one, operator, num_two):
    """Perform calculation based on the operator."""
    if operator == '+':
        return num_one + num_two
    elif operator == '-':
        return num_one - num_two
    elif operator == '*':
        return num_one * num_two
    elif operator == '/':
        if num_two == 0:
            raise ZeroDivisionError(ZERO_DIVISION_ERROR_MSG)
        return num_one / num_two

def write_to_file(filename, content):
    """Write the content to the file."""
    with open(filename, 'a+') as f:
        f.write(content)

def read_from_file(filename):
    """Read the content from the file."""
    with open(filename, 'r') as f:
        return f.read()

try:
    num_one, operator, num_two = get_user_input()
    result = perform_calculation(num_one, operator, num_two)
    write_to_file(FILE_NAME, f"{num_one} {operator} {num_two} = {result}\n")
    print(f'The result for {num_one} {operator} {num_two} is {result}')
except ValueError:
    print(VALUE_ERROR_MSG)
except ZeroDivisionError as e:
    print(e)
finally:
    prev_result = input('Would you like to print previous result? (y/n): ')
    if prev_result.lower() == 'y':
        try:
            print(read_from_file(FILE_NAME))
        except FileNotFoundError:
            print("File does not exist or cannot be found")
