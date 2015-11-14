import matplotlib.pyplot as plt
import seaborn as sns


def plot_columns(df, col_names):
    for column in col_names:
        try:
            plt.title(column)
            df[column].plot()
            plt.figure(figsize = (10,5))
        except:
            print "Cannon plot column", column
