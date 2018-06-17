from options import Options

if __name__ == "__main__":
    options = Options("./config_template.json")

    print(options.output())
    print(options.thread_options())

    for thread_option in options.thread_options():
        pass
