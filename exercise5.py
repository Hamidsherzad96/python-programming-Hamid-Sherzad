#Uppgift: 1, Let the user input a word:
#a: print out the number of letters in the word

word = input(f"Input a word: ")

print("Number of letter in the word is:", len(word))

#b: print out the number of uppercase and lowercase letters of the word

word = input(f"Type a word: ")

upper_case = sum(1 for char in word if char.isupper())
lower_case = sum(1 for char in word if char.islower())

print(f"Number of letters in the word is: {len(word)}")
print(f"Number of uppercases: {upper_case}")
print(f"Number of lowercases: {lower_case}")

#Uppgift: 2, Count the number of words in this sentence:
#: A picture says more than a thousand words, a matematical formula says more than a thousand pictures. 

sentence = "A picture says more than a thousand words, a matematical formula says more than a thousand pictures."

word = sentence.split()
word_count = len(word)
print("Number of word in this sentence is:", (word_count))

#Annorlunda lösning:??

sentence = "A picture says more than a thousand words, a mathematical formula says more than a thousand pictures."
len(sentence.split())

#Uppgift: 3, A palindrome is a sequence of characters that is the same,- 
# -when read forward as backwards (ignoring spaces): 
# Let the user input a sequence of characters and check if it is a palindrome.

s = input("Input a sequence: ")

reverse = s[::-1]

if (s == reverse):
    print(f"Yes it is a palindrome")
else:
    print(f"No it is not a palindrome")

#Annorlunda lösning:

palindrome = input("Skriv in en palindrom: ")
palindrome = palindrome.lower()
palindrome = palindrome.replace(" ", "")

rev = ("".join(reversed(palindrome)))

# print(palindrome)
# print(pal_rev)

if rev == palindrome:
    print("Ditt ord är en palindrom!")
else:
    print("Ditt ordär inte en palindrom.")


#Uppgift: 4, Count the number of vowels in this sentence:
# "Pure mathematics is, in its way, the poetry of logical ideas"

sentence = "Pure mathematics is, in its way, the poetry of logical ideas"

vowels = "aeiouyAEIOUY"
vowel_count = sum(1 for char in sentence if char in vowels)

print("Number of vowels are:", vowel_count)

#Annorlunda lösning:

numberOfVowels = 0
vowels = "aeiouy"
text = "Pure mathematics is, in its way, the poetry of logical ideas"

for letter in text.lower():
    if letter in vowels:
        numberOfVowels +=1

print(f"Number of vowels in text :{text} is, {numberOfVowels}!")


#Uppgift: 5, Let the user input a word and

#a: encrypt the message by replacing each letter with the next letter. 
# If the letter is in the end of the alphabet, use the first letter instead.
#e.g. in Swedish: "höst" > "iatu"

word = input(f"Input a word: ")

encrypt = ""

