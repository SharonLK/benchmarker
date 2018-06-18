import json


class RunningResults:
    def __init__(self, json_to_open="output_template.json"):
        with open(json_to_open) as j:
            self.data = json.load(j)
            self.name = self.data["name"]
            self.stamps = []
            for stamp_arr in self.data["stamps"]:
                self.stamps.append(Stamp(stamp_arr["time_stamp"], stamp_arr["delay"]))


class Stamp:
    def __init__(self, time_stamp, delays):
        self.time_stamp = time_stamp
        self.delays = delays


if __name__ == '__main__':
    res = RunningResults()
