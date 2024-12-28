# 1  Python-Functions What does the len() function do in Python?
#     The len() function is a built in function returns the number of items in an object
#     (strings,list,tuples,sets,dictonaries)
#     When the object is a string, the len() function returns the number of characters in the string.
a='hello'
print(len(a))
# Write a code example using len() to find the length of a list.
list=[32,'hi',True,2]
print(len(list))

# 2 Write a Python function greet(name) that takes a persons name as input and prints "Hello, [name]!".
name=input('Enter your name: ')
def greet():
    print('"Hello,',name,'!"')
greet()
# 3 Write a Python function find_maximum(numbers) that takes a list of integers and returns the
# maximum value without using the built-in max() function.
# Use a loop to iterate through the list and compare values.
numbers=[23,12,66,78,100]
def find_maximum():
  max_value=numbers[0]
  for i in numbers:
    if i > max_value:
        max_value=i
  print('Maximum value of the list is',max_value)
find_maximum()

# 4 Explain the difference between local and global variables in a Python function.
# Write a program where a global variable and a local variable have the same name and show how
# Python differentiates between them.
#       [ Local variables are defined and can only be accessed from within the function and are
#     destroyed when the function returns where as Variables that are defined outside of any function are
#     global variables and these variables can be accessed from anywhere in the program,
#     including from within functions.
#     To explicitly define a variable as global, you can use the global keyword.]
abc= 10 #global variable
def my_function():
    abc = 20   #  local variable
    print("Value of x inside the function (local):", abc)
my_function()
print("Value of x outside the function (global):", abc)

# 5 Create a function calculate_area(length, width=5)that calculates the area of a rectangle.
# If only the length is provided, the function should assume the width is 5.
# Show how the function behaves when called with and without the width argument.
def calculate_area(length, width=5):  #default argument
    area=length * width
    print('Area of the rectangle= ',area)
calculate_area(10,3)