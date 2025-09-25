#Uppgift: 1
#Create a function that takes the base and height of a triangle as input-
#-parameters and returns the area of the triangle:

def triangle(b,h):
    area = 0.5*(b*h)
    return area

print(f"{triangle (2,4)} cm2 area.") #Svar på detta värde: 4.0 cm2 are.

##Uppgift: 2
#a:Create a function that takes two points as input parameters and return the Euclidean between them.

import math

def euclidean_distance (p, q):
    p1, p2 = p
    q1, q2 = q

    #--return (f"The euclidean distance between p and q are: {math.sqrt(p1-q1)**2 + (p2-q2)**2}")

#--print(euclidean_distance((4, 3), (5, 1)))

#b: Let the user input two points. Call the function using the users input points.

import math

def euclidean_distance(p1: tuple, p2: tuple) -> float:
    return math.sqrt((p2[0] - p1[0]**2 + p2[1] - p1[1]**2))

x1 = float(input("Enter x1: "))
y1 = float(input("Enter y1: "))
x2 = float(input("Enter x2: "))
y2 = float(input("Enter y2: "))

p1 = (x1, y1)
p2 = (x2, y2)

distance = euclidean_distance(p1, p2)
#print(f"The euclidean distance between {p1} and {p2} is: {euclidean_distance: 2f}")

#c: Use your function to calculate distances between the origin (0, 0)-
#-and each of these points: (10, 3), (-1, -9), (10, -10), (4, -2), (9, -10).

#Uppgift: 3

import numpy as np
import matplotlib as plt

x = np.linspace(-10,10)

def f(x):               #alternativt med lambda: (f = lambda x: np.pow(x, 2) - 3)
    return np.pow(x,2)-3

#b: # SE ÖVER MED ZOOM!!

def g(x):
    return 4*x-7

def plot():
    plt.title("f(x) = x2 - 3\n g(x) = 4x - 7")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.plot(x, f(x),)
    plt.plot(x, g(x),)

np.pow(f(x), g(x))
np.pow (x,a=-10,b=-10)

## Uppgift: 4
# Create a function that takes a name as an input and:removes all leading and trailing blank spaces-
#-make capitalize the first character of each name, and make the rest lowercase.

name = ["  MaRcUs ", " iDA aNderSon", "OLOF Olofsson            "  ]

def clean(names):
    return [name.strip().title() for name in names]

print(clean(name))

##Uppgift: 5
# Create a function that takes a value as input parameter and- 
#-print out the banknotes and coins in Swedish currency-
#-representing this value:
#Bank notes: (1000, 500, 200, 100, 50, 20, 10, 5, 1)
# Now let the user input a value, and use the function to- 
#-calculate the change.

def calculate_change(amount):
    bank_notes = [1000, 500, 200, 100, 50, 20, 10, 5, 1]
    print(f"\nChange for {amount} kr: ")

    for value in bank_notes:
        count = amount //value
        if count:
            print(f"{count} x {value} kr")
        amount %= value # samma som amount 