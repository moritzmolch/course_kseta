import numpy as np
import matplotlib.pyplot as plt

data = np.loadtxt("data.csv")
plt.title("Polynomial")
plt.plot(
    np.arange(20),
    np.poly1d(np.polyfit(data[:, 0], data[:, 1], 1))(np.arange(20)),
    color="r",
)
plt.pplot(data[:, 0], data[:, 1])
plt.xlabel("p_T (GeV)")
plt.ylabel("number of events")
plt.savefig("plot.png")
