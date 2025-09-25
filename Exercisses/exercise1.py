#UPPGIFT: 1, RÄTTA!
import math

value = int(input("Skriv en siffra: "))

if value == 0:
    print("värdet är 0")
elif value > 0:
    print("värdet är större än 0")
else:
    print("värdet är mindre än noll")

#: Raffes lösning:

i = int(input("Input a number:"))

if i > 0:
    print("Numret är positivt.")
elif i < 0:
    print("Numret är negativt.")
else:
    print("Numret är noll.")

#Uppgift: 2, RÄTTA!

num1 = int(input("Skriv en siffra: "))
num2 = int(input("Skriv en siffra: "))


if num1 < num2:
    print("värdet är mindre:", num1)
elif num2 < num1:
    print("värdet är mindre:", num2)
else:
    print("båda har lika värde")

#uppgift: 3, RÄTTA!

a = float(input("vinkel a: "))
b = float(input("vinkle b: "))
c = float(input("vinkel c: "))

if sum([a, b, c]) == 180:
     print("Triangeln har rätt vinkel. ")

else: 
    print("Vinklarna blir ingen triangel. ")

#Raffes lösning:
print("input three angles")
a, b ,c = float((input), float(input), float(input))

if sum([a, b, c]) != 180:
    print("Angles dont form a triangle!")

elif a == 90 or b == 90 or c == 90:
    print("Triangle has a straight angle")

#avancerat::
any(map(lambda x: x== 90)), #:""very long list")) #om det är fär många "värden".

#Uppgift: 4, RÄTTA!

age = 12
weight = 40

if weight > 40:
    print("Rekommenderad dos är 1-2 tabletter")
elif weight >= 26:
    print("Rekommenderad dso är 1/2 - 1 tablett")
elif weight >= 15:
    print("Rekommenderad dos är 1/2 tablett")
else:
    print("inte rekommenderad (för låg vikt)")

#UPPGIFT: 5a

num = int(input("Skriv en siffra: "))

if num == 0:
    print("Siffran är jämn. ")
else:
    print("siffran är udda. ")

#Uppgift:5b

num = int(input("Skriv en siffra: "))

if num == 0:
    print("Siffran går att dela på 5. ")
else:
    print("Siffran går inte att dela på 5. ")

#Uppgift: 5c

num = int(input("Skriv en siffra: "))

if num == 5 and num != 0:
    print("Siffran går att dela på 5 och udda")
else:
    print("Siffran går inte att dela.")

#Uppgift: 6

weight = 8
length = 55
width = 40
height = 23
dimension = (length*width*height)

weight = float(input("Bagagevikt, kg: "))
length = float(input("Bagage längd, cm: "))
width = float(input("Bagage bredd, cm: "))
height = float(input("Bagagets höjd, cm: "))

if weight <= 8 and length <= 55 and width <= 40 and height <= 23:
    print("Bagaget är tillåtet ombord. ")
else:
    print("Bagaget överskrider vikten tyvärr. ")
