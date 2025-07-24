# This script prints "hello world" to the console
print("hello world")
# we dont need to declare the data type of a variable in python
name = "John"
number = 42
#input from the user
number = input("Enter a number: ")
print("You entered:", number)

# This script takes two numbers as input from the user and prints their sum
num1= input("Enter first number: ")
num2 = input("Enter second number: ")

num1 = int(num1)
num2 = int(num2)
sum = num1 + num2
print("The sum is:", sum)


#loops and conditionals
age = int(input("Enter your age: "))
age = int(age)

if age >= 18:
    print("eligible to vote")
else:
    print("not eligible to vote")
# This script demonstrates a simple loop

#elif conditional

num=84
if num >= 90:
    print("Grade A")
elif num >= 80:
    print("Grade B")
elif num >= 70:
    print("Grade C")    
elif num >= 60:
    print("Grade D")
else:
    print("Grade E")

#loops
for i in range(5):
    print("hello", i)



#This script prints the first 10 numbers of the Fibonacci sequence  
num_1 = 0
num_2 = 1
print(num_1 ,"", end="")
print(num_2 ,"", end="")
for i in range(10):
    num_3 = num_1 + num_2
    print(num_3 ,"", end="")
    num_1=num_2
    num_2=num_3

# This script defines a function that prints a greeting message
# Functions in Python are defined using the 'def' keyword
def username(name):
  print("hello" , name)
username("Atul")

# In Python, functions are blocks of reusable code that perform a specific task. Functions can be classified into different types based on how they are defined and used.

# Here are the **types of functions in Python** with **one example each**:

# ---

### 1. **Built-in Functions**

# Functions that are pre-defined in Python.

# **Example:**
num = [3, 1, 4, 2]
print(len(num))  # Output: 4

### 2. **User-defined Functions**

# Functions created by the user using the `def` keyword.

# **Example:**

# ```python
def greet(name):
    return f"Hello, {name}!"

print(greet("Atul"))  # Output: Hello, Atul!


### 3. **Lambda (Anonymous) Functions**

# Functions defined without a name using the `lambda` keyword.

# **Example:**

# ```python
square = lambda x: x * x
print(square(5))  # Output: 25

### 4. **Recursive Functions**

# Functions that call themselves to solve a problem.

# **Example:**

# ```python
def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n - 1)

print(factorial(5))  # Output: 120


### 5. **Built-in Library Functions**

# Functions available via standard libraries (like `math`, `random`, etc.)

# **Example:**

# ```python
import math
print(math.sqrt(16))  # Output: 4.0

# Would you like to dive deeper into any of these types or see more examples?



#list is a collection of items
#list is ordered and mutable  []

#tuples are ordered and immutable
#tuples are defined using parentheses ()

#dictionary is a collection of key-value pairs
#dictionary is unordered and mutable

student = {
    "name": "Atul",
    "age": 25,
    "marks": 92
}

print(student.get("age"))

# loop through the dictionary and print key-value pairs
for key, value in student.items():
    print(key, ":", value)


# set is a collection of unique items
# set is unordered and mutable

#set operations
# union, intersection, difference, symmetric difference
a = {1, 2, 3}
b = {3, 4, 5}

print(a.union(b))      # {1, 2, 3, 4, 5}
print(a.intersection(b)) # {3}

