# Multiply all the elements in a list
def multiply_list(l):
    if len(l) == 1:
        return l[0]
    else:
        return multiply_list(l[:-1]) * l[-1]

# Return the factorial of n
def factorial(n):
    if n == 1:
        return 1
    else:
        return factorial(n-1) * n 

# Count the number of elements in the list l
def count_list(l):
    if len(l) == 1:
        return 1
    else:
        return count_list(l[:-1]) + 1 

# Sum all of the elements in a list
def sum_list(l):
    if len(l) == 1:
        return l[0]
    else:
        return sum_list(l[:-1]) + l[-1]


# Reverse a list without slicing or loops
def reverse(l):
    if len(l) == 1:
        return l
    else:
        popped = l.pop(0)
        reverse(l).append(popped)
        return l

# Fibonacci returns the nth fibonacci number. The nth fibonacci number is
# defined as fib(n) = fib(n-1) + fib(n-2)
def fib(n):
    if n == 2:
        return 1
    elif n == 1:
        return 0
    else:
        return fib(n-1) + fib(n-2)

# Finds the item i in the list l.... RECURSIVELY
def find(l, i):
    if len(l) == 0:
        return False
    elif l[-1] == i:
        return True
    return find(l[:-1], i)

# Determines if a string is a palindrome
def palindrome(some_string):
    if len(some_string) == 1 or len(some_string) == 0:
        return True
    elif some_string[0] == some_string[-1]:
        return palindrome(some_string[1:-1])
    return False

# Given the width and height of a sheet of paper, and the number of times to fold it, 
# return the final dimensions of the sheet as a tuple. Assume that you always fold in half along the longest edge of the sheet.
def fold_paper(width, height, folds):
    if folds == 0:
        return (width, height)
    elif folds % 2 == 1:
        return fold_paper(width, height / 2.0, folds - 1)
    return fold_paper(width / 2.0, height, folds - 1)

# Count up
# Print all the numbers from 0 to target
def count_up(target):
    if target == -1:
        return
    count_up(target - 1)
    print target