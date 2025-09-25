##Uppgift: 1
#Find the errors in this code to compute the distance between the point-
#- (x,y) and the origin in a cartesian coordinate system.

""" impor numpy as np #This is the example used!

def distance(x,y)
    reurn np.sqrt(x+y)

print(distance([0.5, 0.5]))
"""

import numpy as np

def distance(x,y):
    return np.hypot(0.5, 0.5)


print(f"The distance between (0.5, 0.5) and origin is {distance(0.5, 0.5):.3f}.")

##Uppgift: 2
#Find the errors in this code. Just change the function, don't touch the test program.
"""
def is_fourdigit(number):
    if number//1000 < 10
        return true
    else 
        return false

for number in test_numbers:
    if is_fourdigit(number):
        print(f"{number} is four-digit")
    else:
        print(f"{number} is not four-digit")
"""

def is_fourdigit(number):
    if 1000 <= abs(number) < 10000:
        return True
    else:
        return False

#NÄSTA EXEMPEL
test_numbers = [231, 3124, -4124, -1000,-999, 1001, 10000, -10000, 999]

for number in test_numbers:
    if is_fourdigit(number):
        print(f"{number} is Four-digit")
    else:
        print(f"{number} is not Four-digit")

##Uppgift: 3

