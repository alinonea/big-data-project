import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

def plot(df, x_col, y_col, x_label, y_label):
    # pandas_df = df.select(x_col, y_col).toPandas()

    mock_data = {
        'x_col': np.round(np.random.normal(0, 3, 10000), 2),
        'y_col': np.round(np.random.normal(4, 1, 10000), 2)
    }

    plt.scatter(mock_data['x_col'], mock_data['y_col'])
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.grid(True)
    plt.show()

plot(None, None, None, 'Temperature', 'Delays')