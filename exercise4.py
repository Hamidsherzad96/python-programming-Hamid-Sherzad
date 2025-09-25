#UPPGIFT: 1a

import random

tärninskast = []
for i in range(11):
    tärninskast.append(random.randint(1, 6))

    print(tärninskast)
    
tärninskast.sort

#uppgift: 1b

import random

tärninskast = []
for i in range(11):
    tärninskast.append(random.randint(1, 6))

    tärninskast.sort(reverse=True)
    print(tärninskast)

#UPPGIFT: 1c

import random

tärninskast = []
for i in range(10):

    tärninskast.append(random.randint(1, 6))

print("Maximum value:", max(tärninskast))
print("Minimum value:", min(tärninskast))

#Uppgift: 2a

maträtter = ["Vegetarisk lasagne", "Spaghetti", "fisk", "grönsakssoppa", "pannkakor"]

print(maträtter)

#uppgift: 2b

veckodagar = ["Måndag", "Tisdag", "Onsdag", "Torsdag", "Fredag", "Lördag", "Söndag"]

print(veckodagar)

#Uppgift: 2c

veckodagar = ["Måndag", "Tisdag", "Onsdag", "Torsdag", "Fredag", "Lördag", "Söndag"]
maträtter = ["Vegetarisk lasagne", "Spaghetti", "fisk", "grönsakssoppa", "pannkakor"]

meny = dict(zip(veckodagar, maträtter))
for veckodagar, maträtter in meny.items():

     print(f"{veckodagar}: {maträtter}")

#UPPGIFT: 3a

squares = [x**2 for x in range(-10, 11)]

print(squares)

#uppgift: 3b

import matplotlib.pyplot as plt
import numpy as np

squares = [x**2 for x in range(-10, 11)]

x_axeln = np.array([0, 20.0])
y_axeln = np.array([0, 100])

plt.plot(x_axeln, y_axeln)
plt.title("Plot x = x**2")
plt.xlabel("x_axeln")
plt.ylabel("y_axeln")
plt.show()

#Uppgift: 4a

värden = ["A1", "B1", "C1", "D1", "E1", "F1", "G1", "H1"]

print(värden)

#uppgift: 4b, SE ÖVER

värden = ["A1", "B1", "C1", "D1", "E1", "F1", "G1", "H1"]

list(f"ABCDEFFGH")
print(värden)

#UPPGIFT: 5a

import random as randint
import matplotlib.pyplot as plt

rolls = [randint(1, 6) for i in range(100)]
print(f"The number of outcome six in 100 dice rolls is: {rolls.count(6)}\n")

#Uppgift: 5b, SE ÖVER!
import random as randint

roll_list = [10, 100, 1000, 10000, 100000, 1000000]
outcome_six =[]
probability = []

for rolls in roll_list:
    result: [randint(1, 6) for i in range(rolls)]
