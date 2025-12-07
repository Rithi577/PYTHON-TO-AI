# Day 03 - Functions Practice


# 1. Function without arguments
def greet():
    print("Hello, welcome!")

greet()
greet()



# 2. Function with one argument
def welcome(name):
    print("Welcome", name)

welcome("rithi")
welcome("joshua")  



# 3. Function with two arguments
def add(a, b):
    print("The sum is", a + b)

add(10, 20)
add(30, 30)



# 4. Function to find square
def square(n):
    print("The square is", n * n)

square(2)
square(4)



# 5. Function returning a value
def my_favmovie():
    return "fav movie is leo"

movie = my_favmovie()
print(movie)

