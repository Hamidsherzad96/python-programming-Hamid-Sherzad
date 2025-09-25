#Labb 2:
import math
import numpy as np
import matplotlib.pyplot as plt
import re

def read_test_points(filename):
    with open(filename, "r") as f:
        text = f.read()

    matches = re.findall(r"\(([^)]*)\))", text)
    return [(float(match[0].strip()), float[match[1].strip())) for match in map(lambda m: m.split(","), matches)]
