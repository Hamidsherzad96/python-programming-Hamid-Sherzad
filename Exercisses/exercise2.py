#uppgift: 1

n = -10
while n <= 10:
    print(f"{n}", end = " ")
    n += 1

#Raffes lösning:

i = -10
while i <= 10:
    print(i, end=" ")
    i += 1

#uppgift: 2a

n = 1
sum = 0

for i in range(101):
    sum += i
    n += 1

print (f"{sum}:")

#Raffes lösning:

i = 0
n = 1
while i <= 100:
    n += i +1
    i += 1
print(i)

#annan lösning med: for
sum = 0
n = 1

while n <= 100:
    sum += n
    if n <100:
        print(f"{n} ", end = "+ ")
    else:
        print(f"{n} ", end = "= ")
    n += 1
print(sum)


#uppgift: 2b

sum = 0
for i in range (1, 100, 2):
    sum += i

    print(f"{i}", end = " ")
    if i != 99:
        print("+", end= "")
    if i == 99:
        print(f"{sum}", end = "")

#Raffes lösning:

i = 1
n = 1
while i <= 99:
    n += i +2
    i += 2
print(n)

#uppgift: 3

import random as rnd

guessin_number = rnd.randint(1, 100)

print("Gissa en siffra mellan 1 och 100!")

gissa = 0

while gissa != guessin_number:
    gissa = int(input("Gissa en siffra: "))

    if gissa < guessin_number:
        print("För låg siffra.")
    elif gissa > guessin_number:
        print("För hög siffra.")
    else:
        print("Rätt gissat, {guessin_number}.")

#Raffes lösning:

import random

i =random.randint(1, 100)
n = 0 #eller n = 1

guess = int(input("I'm thinking of a number between 1 and 100, make a guess."))
while True:
    if guess == i:
        print(f"Congratulations, you guesse correct after {n} guesses!")
        break
    else:
        if guess < i:
            print("Thats too small, try again. ")
            n += 1
        elif guess > i:
            print("Thats to big, try again!")
            n += 1
        guess = int(input("Try again."))

#uppgift: 4a

import random

easy_dif = 10
hard_dif = 100





#Uppgift: 5a


#raffes lösning 5a:

import numpy as np

sum([1/np.pow(2,n) for i in range(i)])
n = 0

while n <= 100:
    print(sum([1/np.pow(2.0, i) for i in range(n)]))
    n += 5

#raffes lösning 5b:

import numpy as np

n = 0

while n <= 100:
    print(sum([1/np.pow(-1.0, i) / (2*n+1) for i in range (n)]))
    n += 5