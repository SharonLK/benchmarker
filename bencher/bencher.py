from time import sleep
import argparse
from options import Options
from datetime import datetime


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
        # TODO: Send HTTP request to the given URL
        start = time_millis()
        sleep(0.2)

        print("Sleeping for {} milliseconds before next request".format(options.intervals()[request]))
        sleep(options.intervals()[request] / 1000)
        request += 1
        request %= len(options.intervals())
