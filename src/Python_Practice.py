from main import greetings
from main import greetings as grt
import main
#lets practice with strings


message1 = "Hello World"
message2 = 'Hello World'

"""
this is a multiline comment
can have statements for more than 
few lines
"""

# string formatting
name = "Bob"

greeting_msg1 = "Hello, %s"% name
greeting_msg2 = "Hello, {}".format(name)
greeting_msg3 = f"Hello, {name}" # this one is the most common types

# Slicing Strings

greeting_msg = "Hello World"
print(greeting_msg [-1]) # 'd'
print(greeting_msg [2:7]) # 'llo W'

# string concatenation

name = "Tom"
surname = "Doe"

print (name +" "+surname)# Tom Doe


"""Practice with conditional statements"""


name = "John"
default_auth_message = "Hello,guest!"
auth_message = f"Hello, {name}" if name else default_auth_message
print (auth_message) # 'Hello, John'


# empty data type is false which means they are considered False in rhe boolean context


empty_dict = {}
empty_list = []
empty_string = str()

if empty_dict:
    pass

if not empty_dict:
    # this code will be executed here as the dict is empty
    pass

if not empty_list:
    # this will run
    pass

mylist = [False, True, False]
result_for_any = any(mylist)  #True
result_for_all = all(mylist)  #False
print(result_for_any)
print(result_for_all)


"""Now lets work on collections"""

#working with the list (mutable)

fruit_list = ['apple', 'banana', 'mango']

fruit_list.append('cherry') # insert an element at the last ['apple', 'banana', 'mango', 'cherry']
print (fruit_list)

print(fruit_list[::-1]) # reverse the list ['cherry', 'mango', 'banana', 'apple']

fruit_list[0] = 'watermelon'
print (fruit_list) # ['watermelon', 'banana', 'mango', 'cherry']

#working with the set (mutable)
''' collection without duplicates should use set.'''
fruit_set ={"apple", "banana", "mango"}
fruit_set.add("apple")
print(" fruit set : ",fruit_set) #{'apple', 'banana', 'mango'}

# working with dictionary (mutable)
personal_data = {"name":"john", "age":23}
print(personal_data)
print(personal_data["name"]) #john
print(personal_data.get("name")) #john

# working with the tuple (immutable)
"""
same as list but, but without the ability to change or add value
**tuples are faster than the list
"""
fruit_tuple = ("apple", "banana", "mango")
print(fruit_tuple)
# fruit_tuple[0] = "cherry"  #TypeError: 'tuple' object does not support item assignment


"""Now lets practice on the loops """

fruits = ["apple", "banan", "pear"]  #for loop

for fruit in fruits:
    print(fruit)

i = 1
while i < 5:  # while loop
    print(i)
    i+= 1

# get all the names that start with letter 'A' into a new list
names = ["Amelai", "Bob", "Adam", "John", "Alex"]

certain_names = []

for name in names:
    if name.startswith("A"):
        certain_names.append(name)

# may be follow this way
certain_names = [name for names in names if name.startswith("A")]

"""Now practice on function"""

def sum_func(a,b):
    return a + b

result1 = sum_func(1,3)
print(result1)  #4

#lets see how lambdas work
sum_lambda_func = lambda a, b: a+b
result2 = sum_lambda_func(1,3)
print(result2)  #4

# function with additional optional arguments(for sequence)
def some_func(*args):
    for val in args:
        print(f"Index for {val} is {args.index(val)}")

some_func(*[1,2,3,4])

# Function with additional optional arguments (for dictionary)
def some_func(**kwargs):
    for key, val in kwargs.items():
        print(f"Key'{key}' has value '{val}'")

some_func(**{"name": "John", "age": 26})

#we can use the both the *args and the **kwargs as the
# argument/definition for the function
def function_with_both(*args, **kwargs):
    print("args:", args)
    print("kwargs:", kwargs)

function_with_both(1, 'two', a=3, b=4.0)

# let's work the decorators
def hello_world():
    print("Hello World")

link_to_hello_world = hello_world
link_to_hello_world()

# working with the exception
try:
    result = 1/0

except ZeroDivisionError as exception:
    print(str(exception))  #division by zero

# exception must be instances of a class that derives from the BaseException
"""class MyException(BaseException):
    def __str__(self):
        return "It's my exception"

raise MyException()"""

# working with the module
"""
import main
from main import greetings
from main import greetings as grt

"""


main.greetings("Adnan")  # main has been imported and one function has been called
greetings("Adnan")
grt("Module using the as ")
print (main.duplicate(4))