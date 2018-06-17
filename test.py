from options import Options

if __name__ == "__main__":
    options = Options("./format.json")

    print("Hello World!")
    print(options.url())
    print(options.output())
    print(options.thread_options())

    for thread_option in options.thread_options():
        pass
