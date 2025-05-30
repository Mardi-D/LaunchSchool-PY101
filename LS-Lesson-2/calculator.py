# Ask the user for the first number.
# Ask the user for the second number.
# Ask the user for an operation to perform.
# Perform the operation on the two numbers.
# Print the result to the terminal.

# Helper functions
def prompt(message):
    print(f'==> {message}')


def invalid_number(number_str):
    try:
        int(number_str)
    except ValueError:
        return True

    return False


prompt('Welcome to Calculator!')

prompt('What is the first number?')  # Ask the user for the first number.
number1 = input()

# Confirm user provided valid input for first number.
while invalid_number(number1):
    prompt('Hmmm... That does not look like a valid number.')
    number1 = input()

# Ask the user for the second number.
prompt('What is the second number?')
number2 = input()

# Confirm user provided valid input for second number.
while invalid_number(number2):
    prompt('Hmmm... That does not look like a valid number.')
    number2 = input()

# print(f'{number1} {number2}')

# Perform the operation on the two numbers.
prompt('What operation would you like to perform?\n1) Add 2) Subtract 3) Multiply 4) Divide')
operation = input()

# Validate the operation requested by the user.
while operation not in ["1", "2", "3", "4"]:
    # ask again
    prompt('You must choose 1, 2, 3, or 4')
    operation = input()

# if operation == '1':  # add
#     output = int(number1) + int(number2)
# elif operation == '2':  # subtract
#     output = int(number1) - int(number2)
# elif operation == '3':  # multiply
#     output = int(number1) * int(number2)
# elif operation == '4':  # divide
#     output = int(number1) / int(number2)

# prompt(f'=> The result is {output}')

match operation:
    case '1':
        output = int(number1) + int(number2)
    case '2':
        output = int(number1) - int(number2)
    case '3':
        output = int(number1) * int(number2)
    case '4':
        output = int(number1) / int(number2)

prompt(f'=> The result is {output}')
