try:
    with open('equation.txt', 'a+') as f:
        num_one = int(input('Enter first number: '))
        operator = input('Enter operator: ')
        num_two = int(input('Enter second number: '))

        if operator == '+':
            result = num_one + num_two
        elif operator == '-':
            result = num_one - num_two
        elif operator == '*':
            result = num_one * num_two
        elif operator == '/':
            if num_two == 0:
                raise ZeroDivisionError("Cannot divide by zero")
            result = num_one / num_two

        f.write(f"{num_one} {operator} {num_two} = {result}\n")
        print(f'The result for {num_one} {operator} {num_two} is {result}')
except ValueError:
    print('Oops! Must input an integer')
except ZeroDivisionError as e:
    print(e)
finally:
    prev_result = input('Would you like to print previous result? (y/n): ')
    if prev_result.lower() == 'y':
        try:
            with open('equation.txt', 'r') as f:
                print(f.read())
        except FileNotFoundError:
            print("File does not exist or cannot be found")
        