import functools
import operator
# python code to demonstrate working of reduce()

# initializing list
lis = [1, 3, 5, 6, 2]

# using reduce to compute sum of list
print("The sum of the list elements is : ", end="")
print(functools.reduce(lambda a, b: a + b, lis)) # (((1 + 3) + 5) + 6) + 2 = 17

# using reduce to compute maximum element from list
print("The maximum element of the list is : ", end="")
print(functools.reduce(lambda a, b: a if a > b else b, lis)) # The maximum element of the list is : 6

"""
It starts with the first two elements, compares them, and takes the greater one. 
It then compares this result with the next element in the list, and so on, until the entire list is processed.
For example: max(max(max(max(1, 3), 5), 6), 2) = 6
"""


#lis = [1, 3, 5, 6, 2]
# using reduce to compute sum of list
# using operator functions
print("The sum of the list elements is : ", end="")
print(functools.reduce(operator.add, lis))

# using reduce to compute product
# using operator functions
print("The product of list elements is : ", end="")
print(functools.reduce(operator.mul, lis))

# using reduce to concatenate string
print("The concatenated product is : ", end="")
print(functools.reduce(operator.add, ["geeks", "for", "geeks"]))


"""
output:
    The sum of the list elements is : 17
    The product of list elements is : 180
    The concatenated product is : geeksforgeeks
"""