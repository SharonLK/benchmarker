import json
from collections import namedtuple

Stamp = namedtuple("Stamp", ["time", "delay"])


class RunningResults:
    def __init__(self, json_path="output_template.json"):
        with open(json_path) as f:
            self.data = json.load(f)

            self.name = self.data["name"]
            self.stamps = []
            for stamp in self.data["stamps"]:
                self.stamps.append(Stamp(stamp["time_stamp"], stamp["delay"]))


if __name__ == '__main__':
    res = RunningResults()
