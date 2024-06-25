# Python code to demonstrate dictionary
# comprehension

# Lists to represent keys and values
keys = ['a','b','c','d','e']
values = [1,2,3,4,5]

# but this line shows dict comprehension here
myDict = { k:v for (k,v) in zip(keys, values)}

# We can use below too
# myDict = dict(zip(keys, values))

print (myDict) #{'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}


# Python Filter Function with a Custom Function

#  function that filters vowels
def fun(variable):
    letters = ['a', 'e', 'i', 'o', 'u']
    if (variable in letters):
        return True
    else:
        return False


# sequence
sequence = ['g', 'e', 'e', 'j', 'k', 's', 'p', 'r']

# using filter function
filtered = filter(fun, sequence)

print('The filtered letters are:')
for s in filtered:
    print(s) # The filtered letters are: e e
