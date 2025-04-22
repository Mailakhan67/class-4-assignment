def add(a,b):
    return a + b


import requests
response = requests.get("https://www.example.com")
print(response.status_code)


import math
print(math.pi)  # Output: 3.141592653589793

import numpy as np
print(np.array([1, 2, 3]))

from math import sqrt, pi
print(sqrt(16))  # Output: 4.0
print(pi)        # Output: 3.141592653589793


from math import sqrt as s, pi as p

print(s(16))
print(p )

import math
import numpy as np
print(math.pi)  # math ka pi
print(np.pi)    # numpy ka pi

#conflict wildcard imports avoid
from math import *
from numpy import *
print(pi)



def square(x):
  """this is the parameter of function"""
  return x ** 2
x=float(input("Enter a number:"))
out=square(x)
print('the square of',x, 'is' ,out)
help(square)
