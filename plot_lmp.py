import matplotlib.pyplot as plt
from data_query import data_query


def plot_lmp():
    plot_data = data_query()

    plt.plot(plot_data.iloc[0, 4:27])
    plt.xlabel('Hour Ending')
    plt.ylabel('LMP Values')
    plt.xticks(rotation=90)
    plt.show()


plot_lmp()
