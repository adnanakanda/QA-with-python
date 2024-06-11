

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

# lets work with unoque list
lst = [1, 2, 2, 3, 4, 4]
unique_lst = list(set(lst))  #set cant hold duplicates
print(unique_lst)

# zip() Combines elements from multiple iterables into tuples.
a = [1, 2, 3]
b = ['a', 'b', 'c']
zipped = list(zip(a, b))
print(zipped)  # Output: [(1, 'a'), (2, 'b'), (3, 'c')]
