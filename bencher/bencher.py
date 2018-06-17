from time import sleep
import argparse
from options import Options
from datetime import datetime
import urllib.request


def time_millis() -> int:
    """Return current time in milliseconds

    :return: current time in milliseconds
    """
    return int((datetime.utcnow() - datetime(1970, 1, 1)).total_seconds() * 1000)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--config", help="Path to the configuration file", required=True)

    args = parser.parse_args()

    options = Options(args.config)

    request = 0
    for _ in range(0, int(options.cycles())):
        # Call function and check delay
        start = time_millis()
        f = urllib.request.urlopen(options.url())
        delay = time_millis() - start

        print("Delay: {}".format(delay))

        print("Sleeping for {} milliseconds before next request".format(options.intervals()[request]))
        sleep(options.intervals()[request] / 1000)
        request += 1
        request %= len(options.intervals())
