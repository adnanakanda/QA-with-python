# The format for list slicing is of Python List Slicing is as follows:
"""Lst[ Initial : End : IndexJump ]
        included: excluded:
"""

# Initialize list
Lst = [50, 70, 30, 20, 90, 10, 50]

# we will access the elements of a list using negative indexing.
# Display list
print(Lst[-7::1])  # [50, 70, 30, 20, 90, 10, 50]

# slicing the list
# Display list
print(Lst[1:5]) #[70, 30, 20, 90] from index 1 to 5 but the index 5 is excluded

print(Lst[1::2])

"""
A Python list comprehension consists of brackets containing the expression, 
which is executed for each element along with the for loop to iterate over each element in the Python list. 
"""

numbers = [12, 13, 14,]
doubled = [x *2 for x in numbers]
print(doubled)

# Using lambda and map to double the numbers
squared = list(map(lambda x: x ** 2, numbers))
print(squared)  # Output: [144, 169, 196]

# Even list using List Comprehension
lst = [i*2 for i in range(1,12)]
print(lst)
lst = [i*2 for i in range(1,12) if i % 2 == 0]
print(lst)  # [2, 4, 6, 8, 10]


numbers = [1, 2, 3, 4, 5, 6]
even_numbers = filter(lambda x: x % 2 == 0, numbers)
print(list(even_numbers))
