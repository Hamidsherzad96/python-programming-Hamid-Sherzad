#Uppgift: 1a
import math

a = 3
b = 4

c = math.sqrt(a**2 + b**2)

print(c)

#Uppgift: 1b

import math

c = 7.0
a = 5.0

b = math.sqrt(c**2 - a**2)

print(b)

# annorlunda "lösning"
print(f"Länged av katetern b är{b: .1f} cm.")

#uppgift: 2

x = 300
y = 365

accuracy = x/y

print (accuracy)

#alternativt utförligare
procent = accuracy*100

print(f"Träffsäkerheten av modellen är{procent:.2f}%.")

#uppgift: 3

tp = 2
fp = 2
fn = 11
tn = 985

accuracy = (tp+tn)/(tp+tn+fp+fn)

print(accuracy)

#alternativt:
print(f"{accuracy: .2f}")

#Uppgift: 4

x1=4
y1=4
x2=0
y2=1

k=(y2-y1)/(x2-x1)
m = y2-k*x2

print(f"Formeln för linjen är y={k}x+{m:.0f}.\n")

k = (4-1)/(4-0)

print(k)

#annorlunda lösning:

a = (4,4)
b = (0,1)

#Uppgift: 5

p1 = (3, 5)
p2 = (-2, 4)

distance = math.sqrt((p2[0]-p1[0])**2+(p2[1]-p1[1])**2)

print(f"Längden är {distance:.1f}cm")

#annorlunda lösning:

P = (3, 5)
Q = (-2,4)

p1 = 3
p2 = 5
q1 = -2
q2 = 4

d = math.sqrt((p1-q1)**2 + (p2 - q2)**2)

print(d)

#Uppgift: 6

p1 = (2, 1, 4)
p2 = (3, 1, 0)

distance = math.sqrt((p1[0]-p2[0])**2 + (p1[1]-p2[1])**2 + (p1[2]-p2[2])**2)

print(f"Längden mellan de två punkterna är ca {distance:.2f}")

#annorlunda lösning


#Klappat och klart 