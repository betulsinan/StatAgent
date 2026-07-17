import matplotlib.pyplot as plt
import pandas as pd


def histogram(df, column):

    if column is None:
        return None

    fig, ax = plt.subplots(figsize=(8,4))

    df[column].hist(ax=ax)

    ax.set_title(f"{column} Histogramı")

    ax.set_xlabel(column)
    ax.set_ylabel("Frekans")

    return fig


def boxplot(df, column):

    if column is None:
        return None

    fig, ax = plt.subplots(figsize=(8,4))

    ax.boxplot(df[column].dropna())

    ax.set_title(f"{column} Box Plot")

    ax.set_ylabel(column)

    return fig


def scatter_plot(df, x_col, y_col):

    if x_col is None or y_col is None:
        return None

    fig, ax = plt.subplots(figsize=(8,4))

    ax.scatter(df[x_col], df[y_col])

    ax.set_xlabel(x_col)
    ax.set_ylabel(y_col)

    ax.set_title(f"{x_col} vs {y_col}")

    return fig


def correlation_matrix(df):

    numeric = df.select_dtypes(include="number")

    if len(numeric.columns) < 2:
        return None

    corr = numeric.corr()

    fig, ax = plt.subplots(figsize=(6,5))

    image = ax.imshow(corr)

    ax.set_xticks(range(len(corr.columns)))
    ax.set_xticklabels(corr.columns, rotation=45)

    ax.set_yticks(range(len(corr.columns)))
    ax.set_yticklabels(corr.columns)

    plt.colorbar(image)

    ax.set_title("Korelasyon Matrisi")

    return fig