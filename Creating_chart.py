# Implementation of matplotlib function
import matplotlib
import matplotlib.pyplot as plt
import numpy as np


def save_as_csv(X, Y):
    # importing pandas as pd
    import pandas as pd

    # dictionary of lists
    dict = {'Rarety': X, 'IQ': Y}

    df = pd.DataFrame(dict)

    # saving the dataframe
    df.to_csv('IQ_Rarity.csv', header=True, index=False)

    return 0


def show():
    plt.xlabel('X Axis')
    plt.ylabel('Y Axis')

    plt.title('hist() function Example\n\n', fontweight="bold")

    plt.show()


np.random.seed(10**7)
mu = 121
sigma = 21
x = mu + sigma * np.random.randn(1000)

num_bins = 100

n, bins, patches = plt.hist(x, num_bins, density=10, color='green')

print(len(n), len(bins))
save_as_csv(bins[1:], n)

# y = ((1 / (np.sqrt(2 * np.pi) * sigma)) *np.exp(-0.5 * (1 / sigma * (bins - mu))**2))

# plt.plot(bins, y, '--', color ='black')

# show()
