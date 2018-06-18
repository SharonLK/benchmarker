import matplotlib.pyplot as plt
from plotting.running_results import RunningResults


class Plotting:
    def __init__(self, result: list):
        self.result = result
        self.ax = plt.subplot()

    def plot_bars(self):
        for result in self.result:
            for stamp in result.stamps:
                self.ax.bar(stamp.time, stamp.delay, width=10, color='b')

        plt.show()


if __name__ == '__main__':
    plot = Plotting([RunningResults()])
    plot.plot_bars()
