import numpy as np
import matplotlib.pyplot as plt


DATA_PATH = "data.csv"
OUTPUT_PATH = "plot.png"

def load_data(data_path):
    return np.loadtxt(data_path)


def plot(data, output_path):
    plt.title("Polynomial")
    plt.plot(
        np.arange(20),
        np.poly1d(np.polyfit(data[:, 0], data[:, 1], 1))(np.arange(20)),
        color="r",
    )
    plt.scatter(data[:, 0], data[:, 1])
    plt.xlabel("p_T (GeV)")
    plt.ylabel("number of events")
    plt.savefig(output_path)


if __name__ == "__main__":
    data = load_data(DATA_PATH)
    plot(data, OUTPUT_PATH)

