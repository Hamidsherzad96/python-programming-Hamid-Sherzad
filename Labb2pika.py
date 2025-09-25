import math     #Har använt mig av lecture notes, w3school,  och exercisen som vi har övat på. Även bollat lite med klasskamraterna.
                #Fick hjälp med strukturen och bantningen av koden av en vän till mig som jobbar inom denna bransch och han har-
                #10-års erfarenhet/kunskaper inom python-programmering.
import numpy as np
import matplotlib.pyplot as plt
import re

def read_test_points(filename):
    #Öppnar filen och läser allt som en enda String.
    with open(filename, 'r') as f:
        text = f.read()

    matches = re.findall(r"\(([^)]*)\)", text)
    return [(float(match[0].strip()), float(match[1].strip())) for match in map(lambda m: m.split(','), matches)]


def distance(p1, p2) -> float:                                      
    #Här tillämpar jag Euclidean distance formeln, för att beräkna avståndet mellan punkterna.
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2) 



def split_data(data):   
    #splittar på datan här så de blir 2 grupper.
    pichu = [(x, y) for (x, y, n) in data if n == 0]
    pikachu = [(x, y) for (x, y, n) in data if n == 1]

    return pichu, pikachu


def plot_points(pichu, pikachu):
    # Unpack tuples into x and y listor
    x1, y1 = zip(*pichu)
    x2, y2 = zip(*pikachu)

    # Scatter plot
    plt.scatter(x1, y1, color="blue", label="Pichu", marker="o")
    plt.scatter(x2, y2, color="red", label="Pikachu", marker="x")

    plt.xlabel("X-axis")
    plt.ylabel("Y-axis")
    plt.title("Two Datasets as Points")
    plt.legend()
    plt.show()


def classify(test_points, pichu, pikachu):
    #Beräknar avståndet från p till varje Pichu-punkt och tar det minsta → d_pichu.
    #Samma för pikachu.
    for p in test_points:
        d_pichu = min(map(lambda x: distance(x, p), pichu))
        d_pikachu = min(map(lambda x: distance(x, p), pikachu))
    #Bestämmer det avstånd som är mindre avgör vilken klass de tillhör.
        character_type = 'Pichu' if d_pichu < d_pikachu else 'Pikachu'
        print(f'Sample with (width, height): {p} classified as {character_type}')

    #Sätter ihop allting, laddar datapoints, testpoints och klassifierar varje test point.
def main():
    data = np.genfromtxt('datapoints.txt', delimiter=',', names=True)
    test_points = read_test_points('testpoints.txt')

    pichu, pikachu = split_data(data)

    plot_points(pichu, pikachu)

    classify(test_points, pichu, pikachu)


main()

#breakpoint ??
#def ask_user_points():
    #while True:
        #try:
           # x = float(input("Mata in bredd (x): "))
           # y = float(input("Mata in häjd (y): "))