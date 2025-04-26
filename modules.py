# def add(a,b):
#     return a + b


# import requests
# response = requests.get("https://www.example.com")
# print(response.status_code)


# import math
# print(math.pi)  # Output: 3.141592653589793

# import numpy as np
# print(np.array([1, 2, 3]))

# from math import sqrt, pi
# print(sqrt(16))  # Output: 4.0
# print(pi)        # Output: 3.141592653589793


# from math import sqrt as s, pi as p

# print(s(16))
# print(p )

# import math
# import numpy as np
# print(math.pi)  # math ka pi
# print(np.pi)    # numpy ka pi

# #conflict wildcard imports avoid
# from math import *
# from numpy import *
# print(pi)



# def square(x):
#   """this is the parameter of function"""
#   return x ** 2
# x=float(input("Enter a number:"))
# out=square(x)
# print('the square of',x, 'is' ,out)
# help(square)


def  greeting():
   'my function'
   greet='hello world'
   return greet

message=greeting()
print(message)




def modify_value(x):
    x = 10
    print("Within function:", x)

# Immutable object (integer)
x = 5
print("Original:", x)
modify_value(x)
print("After function:", x)


# Argumnets and parameter

def greetings(name):
       "This is docstring of greetings function"
       print ("Hello {}".format(name))
       return

greetings("Ali")
greetings("Omar")
greetings("Usman")



# keyword arguments

def printinfo( name, age ):
       "This prints a passed info into this function"
       print ("Name: ", name)
       print ("Age ", age)
       return;

# Now you can call printinfo function
printinfo( age=50, name="Arif" )
#printinfo(50, "Arif" )





def add(x: int,y: int=0) -> float:
       return float(x + y)

print(float(add(10,20)))

print(add(y=50.0, x=2.0)) # type hints are not enforced in Python

print(add(x=5))




def show(*x):
    print(x)


show(*['maila','naila'])
show(1, 2, 3, 'm')




def my_sum(*nums):
      print(type(nums),", ", nums)

      return sum(nums)

print("Sum     = ", my_sum(1,2,3,4,5,8,5),"\n")
print("Sum *[] = ", my_sum(*[1,2,3,4,5,8,5]), "\n") # *  unpacking list
print("Sum *() = ", my_sum(*(1,2,3,4,5,8,5))) # *  unpacking tuple





# Default arguments

def printinfo( name, age = 35 ):
       "This prints a passed info into this function"
       print ("Name: ", name)
       print ("Age ", age)
       return;

# Now you can call printinfo function
printinfo( age=50, name="Arif" )
printinfo( name="Arif" )


def main(x,y,/,b,c):
      return x + y +b+c
print(main(3,2,2,c=1))



#keyword only arguments
def main(*,a,b):
    print(a+b)
    return
print(main(b=2,a=5))



#Posional-only-arguments
def func(a,b,/):
      print(a+b)

func(5,5)
      

def com(a,b,/,*,c,d):
      print(a+b)
      print(c+d)

com(1,1,c=2,d=2)


def greet_all(*names):
    for name in names:
        print("Hello", name)

greet_all("Ali", "Sara", "Ahmed")


def demo(*args):
    print(args)

demo(1, 2, 3)




