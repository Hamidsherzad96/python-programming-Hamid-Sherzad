#UPPGIFT: 1

for i in range(-10, 11):
    print (f"{i}", end= " ")

#UPPGIFT: 1b

x = -10
y = 11

for i in range(x, y, 2):
    print(f"{i}", end = " ")

#UPPGIFT: 2a

sum = 0

for i in range(1, 101):
    sum += i
print(sum) 

#uppgift: 2b

sum = 0

for i in range(1, 100, 2):
    sum += i
print(sum)

#UPPGIFT: 3a

for i in range(1, 11):
    numeric = i*6
    print(f"{numeric}", end = " ")

#uppgift: 3b

table = int(input("Vilket bord väljer du?: "))
start = int(input("Vart på bordet vill du starta?: "))
end = int(input("Vart slutar bordet?: "))

for i in range(start, end+1):
    produkten = i*table
    print(produkten)

#uppgift: 3c
#SE ÖVER UPPGIFT!
for x in range(11):
    for y in range(11):
        print(f"{y * x}")
    print()

#UPPGIFT: 4

n = int(input("Välj siffra: "))
y = 1

for i in range(1, n+1):
    y *= i
print(f"Multiplikationen av {n} är {y}")

#UPPGIFT: 5, SE ÖVER!

import random

siffran = random.randint(1500, 3000)
print("Datorn har valt en siffra mellan 1500-3000.")

for gissa in range(1500, 3001):
    if gissa == siffran:
        print(f"Rätt svar, siffran var {siffran}")
        break

#UPPGIFT 6:

rutor = 64
riskorn = 0

for i in range(rutor):
    riskorn += 2**i

    print(f"{riskorn} antal korn.")
