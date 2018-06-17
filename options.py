import json


class Options:
    def __init__(self, file):
        with open(file, "r") as f:
            self.j = json.load(f)

    def output(self):
        return self.j["output"]

    def url(self):
        return self.j["url"]

    def name(self):
        return self.j["name"]

    def intervals(self):
        return self.j["intervals"]

    def cycles(self):
        return self.j["cycles"]
