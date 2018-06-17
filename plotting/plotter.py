import matplotlib.pyplot as plt
from plotting.running_results import RunningResults


class Plotting:
    def __init__(self, running_result_list: list):
        self.x = 0
        sum_stamps = 0
        self.running_result_list = running_result_list
        for result in running_result_list:
            for stamp in result.stamps:
                if self.x < stamp.time_stamp:
                    self.x = stamp.time_stamp
                sum_stamps += 1

        #self.width = self.x/sum

        self.multiple_bars = plt.figure()
        self.ax = plt.subplot()

    def plot_bars(self):
        for result in self.running_result_list:
            for stamp in result.stamps:
                self.ax.bar(stamp.time_stamp, stamp.delays, width=stamp.delays, color='b', align='center')

        plt.show()


if __name__ == '__main__':
    rr = RunningResults()
    plot = Plotting([])
    plot.plot_bars()


