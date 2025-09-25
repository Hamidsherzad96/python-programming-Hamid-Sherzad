import numpy as np
import matplotlib as plt

x = np.linspace(-10,10)

def f(x):               #alternativt med lambda: (f = lambda x: np.pow(x, 2) - 3)
    return np.pow(x,2)-3

def g(x):
    return 4*x-7

def plot():
    plt.title("f(x) = x2 - 3\n g(x) = 4x - 7")
    plt.xlabel("X-axis")
    plt.ylabel("Y-axis")

    plt.plot(x, f(x), label = "f(x) = $x^2 - 3$")
    plt.plot(x, g(x), label = "g(x) = 4x - 7")
    plt.scatter(2, 1, label = "Tangency", color = "red")
    plt.legend()

plot()

names = ["  MaRcUs ", " iDA aNderSon", "OLOF Olofsson            "  ]

def clean_name(name):
    name = name.strip()
    name = name.title()

    return(name)