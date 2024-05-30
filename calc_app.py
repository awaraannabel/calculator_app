# Constants
FILE_NAME = 'equation.txt'
ZERO_DIVISION_ERROR_MSG = "Cannot divide by zero"
VALUE_ERROR_MSG = 'Oops! Must input an integer'

try:
    # Open the file in append mode
    with open(FILE_NAME, 'a+') as f:
        # Input first number
        num_one = int(input('Enter first number: '))
        # Input operator
        operator = input('Enter operator: ')
        # Input second number
        num_two = int(input('Enter second number: '))

        # Perform the calculation based on the operator
        if operator == '+':
            result = num_one + num_two
        elif operator == '-':
            result = num_one - num_two
        elif operator == '*':
            result = num_one * num_two
        elif operator == '/':
            if num_two == 0:
                raise ZeroDivisionError(ZERO_DIVISION_ERROR_MSG)
            result = num_one / num_two

        # Write the result to the file
        f.write(f"{num_one} {operator} {num_two} = {result}\n")
        print(f'The result for {num_one} {operator} {num_two} is {result}')
except ValueError:
    # Handle invalid integer input
    print(VALUE_ERROR_MSG)
except ZeroDivisionError as e:
    # Handle division by zero
    print(e)
finally:
    # Ask if the user wants to print previous results
    prev_result = input('Would you like to print previous result? (y/n): ')
    if prev_result.lower() == 'y':
        try:
            # Open the file in read mode and print its contents
            with open(FILE_NAME, 'r') as f:
                print(f.read())
        except FileNotFoundError:
            # Handle file not found error
            print("File does not exist or cannot be found")

        