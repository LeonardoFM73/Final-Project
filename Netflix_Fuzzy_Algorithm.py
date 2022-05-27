import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import math
import copy

netflix = pd.read_csv('netflix_titles.csv')
X = netflix.iloc[:, 1:].values

print(netflix)
