import matplotlib.pyplot as plt
from plotting.running_results import RunningResults


class Plotting:
    def __init__(self, running_result_list: list):
        self.running_result_list = running_result_list
        self.ax = plt.subplot()

    def plot_bars(self):
        for result in self.running_result_list:
            for stamp in result.stamps:
                self.ax.bar(stamp.time_stamp, stamp.delays, width=10, color='b')

        plt.show()


if __name__ == '__main__':
    plot = Plotting([RunningResults()])
    plot.plot_bars()
