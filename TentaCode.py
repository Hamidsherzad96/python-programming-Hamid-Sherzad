##Break statement, osv.
import random as rnd # this module has functions for generating random numbers 

while True: 
    number1 = rnd.randint(1,10)
    number2 = rnd.randint(1,10)

    user_answer = int(input(f"What is {number1}*{number2}? "))
    if user_answer == number1*number2:
        print("Correct")
    else:
        print(f"{user_answer} is unfortunately wrong")

    play_again = input("Wanna play again (y for yes)? ")
    
    if play_again != "y":
        print("Have a nice day!")
        break

## RANGE FUNCTION!!
    sum = 0
# calculate sum of all odd numbers between 1 and 100
for i in range(1,20,2):
    sum += i # addition

    # nice printing
    print(f"{i}", end = "")
    if i != 19:
        print("+", end="")

    if i == 19:
        print(f"={sum}", end="")


##ENUMERATE

print("My favorite fruits are: ")
# enumerate to get a number for each element in a list that you loop through

for i, fruit in enumerate(fruits,[1]): # 1 gives the starting number
    print(f"{i}. {fruit}")


## NESTED FOR LOOP'

# matrix coordinates
out = []
for x in range(0,3):
    for j in range(0,3):
        out += [(x,j)]
        print(f"({x},{j})", end="")    
    print() #då skrivs alla värdena ut i (("Parantes"))

print(out)

## CHANGE LIST ITEMS

tv_shows = ["Antikrundan", "Mästerkockarna", "Aktuellt" , "Talang"]
tv_shows[0] = "Vetenskapens värld" #ersätter "Antikrundan[0]" med "Vetenskapens värld"
print(f"Replaced first element: {tv_shows}") 

tv_shows.append("Pokemon") #Lägger till "pokemon" i tv_shows
print(f"Added an element: {tv_shows}")
tv_shows.insert(2, "test#")
print(tv_shows)
# Replaced first element: ['Vetenskapens värld', 'Mästerkockarna', 'Aktuellt', 'Talang']
#Added an element: ['Vetenskapens värld', 'Mästerkockarna', 'Aktuellt', 'Talang', 'Pokemon']
#['Vetenskapens värld', 'Mästerkockarna', 'test#', 'Aktuellt', 'Talang', 'Pokemon']

## SLICING OPERATOR
tv_shows = ["Antikrundan", "Mästerkockarna", "Aktuellt" , "Talang"]

print(tv_shows[1:3]) #["Mästerkockarna, "Aktuellt]

## SORTED NUMBERS

numbers = [21,3,-321,2,0,0]
print(f"Unsorted: {numbers}") #Unsorted: [21, 3, -321, 2, 0, 0]

sorted_numbers = sorted(numbers)
numbers.sort() # in-place
print(f"Sorted: {numbers}, {sorted_numbers}") #Sorted: [-321, 0, 0, 2, 3, 21], [-321, 0, 0, 2, 3, 21]

numbers.sort(reverse=True)
print(f"Sorted descending: {numbers}") #Sorted descending: [21, 3, 2, 0, 0, -321]

## PLOT GRAPH

import matplotlib.pyplot as plt 

x = list(range(10)) # creates a list of integers from 0-9
k = 2
m = 2
y = [k*x+m for x in x]

plt.plot(x,y) # plots y vs x 
plt.title("Plot y = 2x+2")
plt.xlabel("x")
plt.ylabel("y")

## # zip function, two lists to one list of tuples

A_list = [2,3,4]
B_list = ['a','b','c']
C_list = [7,8,9]

tuple_list = list(zip(A_list, B_list, C_list))

print(tuple_list)

print(list(zip(*tuple_list)))
# [(2, 'a', 7), (3, 'b', 8), (4, 'c', 9)]
# [(2, 3, 4), ('a', 'b', 'c'), (7, 8, 9)]

## CONCATENATE STRINGS

firstname = "Kokchun"
lastname = "Giang"

fullname = firstname + " " + lastname # concatenating strings
school = "IT-Högskolan"
address = "Ebbe Lieberathsgatan 18C, 412 65 Göteborg"
phone = "112"

# multiline f-string, # påbörjar f-stringen med 3st =  """ och avslutar med 3st = """.
contact_details = f""" 
Name: {fullname}
School: {school}
Adress: {address}
Phone: {phone}
"""

print(contact_details) #får fram allt som är inom Contact details: f"""
#Name: Kokchun Giang
#School: IT-Högskolan
#Adress: Ebbe Lieberathsgatan 18C, 412 65 Göteborg
#Phone: 112

## CONCATENATE WITH LOOP
bamba = ["Chili sin carne", "Nudlar", "Pokebowl", "Pannkakor", "Tacos"]
days = ["Må", "Ti", "On", "To", "Fr"]

menu = "Veckomeny\n" # \n gives newline

for day, food in zip(days, bamba):
    menu += f"{day}: {food} \n" #man får dagarna på vänster sida och maträtten på högersida med : mellan orden.

print(menu)
#Veckomeny           #:\n gives newline!
#Må: Chili sin carne 
#Ti: Nudlar 
#On: Pokebowl 
#To: Pannkakor 
#Fr: Tacos 

## INDEXING
# note the different types of quotes, can't use '' for denoting string here, as ' is already used
quote = "!False - it's funny because it's True" 
print(f"quote[0]: {quote[0]}")
print(f"quote[5]: {quote[5:10]}") # [start:end-1]
print(f"quote[-4]: {quote[-4]}") # indexing starting from the end
print(f"quote[-4:]: {quote[-4:]}") # slice from -4 to the end
print(f"Backwards quote[::-1]: {quote[::-1]}") # reversing = baklänges ("!False - it's funny because it's True")

## SPLIT A STRING
subjects = "Math, biology  ,   cHeMistry  ,  PrOgramming      "
subjects = subjects.split(",") # argument defines the pattern which the string should be splitted

subjects = [subject.strip().upper() for subject in subjects] # strips and make uppercase

for subject in subjects: 
    print(f"{subject} has {len(subject)} letters") 
    # len() returns the number of items, for a string it returns the number of characters

## 