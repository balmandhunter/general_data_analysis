import matplotlib.pyplot as plt
import seaborn as sns


def plot_params():
    size = 22
    a = plt.rc('xtick', labelsize = size)
    b = plt.rc('ytick', labelsize = size)
    return a, b, plt.gca(), size


def plot_columns(df, col_names):
    plt.figure(facecolor='w', figsize = (5,5))
    a, b, axes, label_size = plot_params()
    for column in col_names:
        try:
            plt.title(column)
            df[column].plot()
            plt.figure(figsize = (5,5))
        except:
            print "Cannot plot: ", column


def plot_column_hist(df, col_names):
    plt.figure(facecolor='w', figsize = (5,5))
    a, b, axes, label_size = plot_params()
    for column in col_names:
        try:
            plt.title(column)
            df[column].hist()
            plt.figure(figsize = (5,5))
        except:
            print "Cannot plot: ", column
