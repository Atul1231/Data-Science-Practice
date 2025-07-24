#list comprehension is a concise way to create lists
squares = [i*i for i in range(1,10)]
print(squares)

#with if condition
squares_even = [i*i for i in range(1,10) if i%2 == 0]
print(squares_even)


#lambda functions are anonymous functions
# they are defined using the 'lambda' keyword
add = lambda x, y: x + y
print(add(5, 3))

multiply = lambda x,y : x*y
print(multiply(2,3))

#---------------------------------------------------------------------#
#lambda with map function
numbers = [1, 2, 3, 4, 5]
squared_numbers = list(map(lambda x: x**2, numbers))
print(squared_numbers)
#---------------------------------------------------------------------#
#lambda with filter function
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(even_numbers)


#file handling in Python
# Python provides built-in functions to handle files
# 'open' function is used to open a file
# 'read', 'write', and 'append' modes are available
# 'read' mode is used to read the contents of a file
# 'write' mode is used to write to a file (overwrites existing content)
# 'append' mode is used to add content to the end of a file
# 'close' method is used to close the file after operations are done
# Example of file handling in Python
# Open a file in write mode and write some text to it
f = open("myfile.txt", "w")   # 'w' = write mode
f.write("Hello, Atul!\nWelcome to Python.")
f.close()

# Open the file in read mode and print its contents
f = open("myfile.txt", "r")   # 'r' = read mode
content = f.read()
print(content)



#class and object in Python
# Python is an object-oriented programming language
# Classes are blueprints for creating objects
# Objects are instances of classes

class Car:
    def __init__(self, brand, year):
        self.brand = brand
        self.year = year

    def start(self):
        print(f"The {self.brand} ({self.year}) car has started.")

# Creating an object of Car
my_car = Car("Toyota", 2020)

# Calling the start method
my_car.start()

