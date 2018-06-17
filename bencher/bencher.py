from time import sleep
import argparse
from options import Options
from datetime import datetime
import urllib.request
import json


def time_millis() -> int:
    """Return current time in milliseconds

    :return: current time in milliseconds
    """
    return int((datetime.utcnow() - datetime(1970, 1, 1)).total_seconds() * 1000)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--config", help="Path to the configuration file", required=True)
    args = parser.parse_args()

    # Parse the configuration file
    options = Options(args.config)

    # Dictionary holding the data gathered from the test (delays, etc...)
    data = {
        "name": options.output(),
        "stamps": []
    }

    request = 0
    start = time_millis()
    for _ in range(0, int(options.cycles())):
        # Call function and check delay
        before = time_millis()
        f = urllib.request.urlopen(options.url())
        delay = time_millis() - before

        data["stamps"].append({
            "time_stamp": before - start,
            "delay": delay
        })

        print("Sleeping for {} milliseconds before next request".format(options.intervals()[request]))
        sleep(options.intervals()[request] / 1000)
        request += 1
        request %= len(options.intervals())

    # Output the data as a JSON file to the output file configured in the configuration file
    with open(options.output(), "w") as f:
        json_data = json.dump(data, f, indent=4)
