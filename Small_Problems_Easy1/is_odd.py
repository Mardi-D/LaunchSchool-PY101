'''Write a function that takes one integer argument and returns True when the number's absolute value is odd, False otherwise.

Problem : Supply an integer and return a Boolean True if int is odd and Boolean False otherwisee. 
input - one integer, output - a Boolean True is number abs() is odd and Boolean False if even or something else.  || 
Requirement - Argument must an integer, no floats, strings or any other type.  Rules - function takes a integer, checks the integer's absolute
value, function can take a negative number
mental model - 
Example: is_odd(100) - False   is_odd(7) - True
Data structure : function returns a boolean,  return True or False
Algorithm - We can use the remainder(modulo operator to check if there is a remainder when divided by 2, if remainder is 0 number
is even, if remainder 
Code with intent: see below...

'''


def is_odd(num):
    if abs(num) % 2 != 0:
        return True
    else:
        return False


odd = is_odd(-201976)
print(odd)
