import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

def plot_boxplot(df, n_rows, n_cols, figsize=(18, 24)):
    numeric_columns = df.select_dtypes(include=np.number).columns
    fig, axn = plt.subplots(n_rows, n_cols, figsize=figsize)
    for col, ax in zip(numeric_columns, axn.flatten()):
        sns.boxplot(df[col], orient='v', ax=ax)
