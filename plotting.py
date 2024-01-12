import matplotlib.pyplot as plt
import pandas as pd


def plot(x_col, y_col, x_label, y_label, title, figure):

    plt.figure(figure)
    plt.scatter(x_col, y_col)
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.grid(True)
    plt.title(title)

    plt.show()