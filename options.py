import json
from collections import namedtuple

ThreadOption = namedtuple("ThreadOption", ["url", "name", "intervals", "requests"])


class Options:
    def __init__(self, file):
        with open(file, "r") as f:
            self.j = json.load(f)

    def output(self):
        return self.j["output"]

    def thread_options(self):
        options = []

        for thread_option in self.j["threads"]:
            options.append(ThreadOption(thread_option["url"],
                                        thread_option["name"],
                                        thread_option["intervals"],
                                        thread_option["requests"]))

        return options
