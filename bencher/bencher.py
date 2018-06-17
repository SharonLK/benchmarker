from threading import Thread
from time import sleep
import argparse
from options import Options, ThreadOption


def handler(thread_option: ThreadOption):
    """Handler for the different threads that are executed in the test

    :param thread_option: options for this thread
    :return: None
    """
    request = 0
    for _ in range(0, len(thread_option.requests)):
        # TODO: Send HTTP request to the given URL

        print("Sleeping for {} milliseconds before next request".format(thread_option.intervals[request]))
        sleep(thread_option.intervals[request] / 1000)
        request += 1
        request %= len(thread_option.intervals)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--config", help="Path to the configuration file", required=True)

    args = parser.parse_args()

    options = Options(args.config)

    # Create thread for each configured thread option and run the handler
    for option in options.thread_options():
        thread = Thread(target=handler, args=(option,))
        thread.start()
        thread.join()
