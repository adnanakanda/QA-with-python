# working with list manipulation

lst = [2, 1, 3, 42, 2, 3, 2]  #need to remove the duplicates from the list w/o changing the order

list_without_duplicates = list(dict.fromkeys(lst))
"""
changes the list into dict type which is immutable and fromkeys creates
new dictionary from the 'lst' with all values set to 'none' 
{2: None, 1: None, 3: None, 42: None}
then the whole thing is changed back into the list.
"""
print(list_without_duplicates)

# let's work with unique list
lst = [1, 2, 2, 3, 4, 4]
unique_lst = list(set(lst))  #set cant hold duplicates
print(unique_lst)

# zip() Combines elements from multiple iterables into tuples.
a = [1, 2, 3]
b = ['a', 'b', 'c']
zipped = list(zip(a, b))
print(zipped)  # Output: [(1, 'a'), (2, 'b'), (3, 'c')]

# map()
lst = [1, 2, 3, 4]
squared = list(map(lambda x: x ** 2, lst))  #Applies a function to all items in an input list.
print(squared)  # Output: [1, 4, 9, 16]

# filter()
lst = [1, 2, 3, 4]
even_numbers = list(filter(lambda x: x % 2 == 0,lst))  #Constructs an iterator from elements of an iterable for which a function returns true.
print(even_numbers)  # Output: [2, 4]

# enumerate()
lst = ['a', 'b', 'c']
for index, value in enumerate(lst):  #Adds a counter to an iterable and returns it as an enumerate object.
    print(index, value)
# Output:
# 0 a
# 1 b
# 2 c

t1 = (1, 2)
t2 = (3, 4)
t = t1 + t2
print(t)  # Output: (1, 2, 3, 4)
a, b, c, d = t
print(a, b, c, d)  # Output: 1 2 3 4
