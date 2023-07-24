
if __name__ == "__main__":
    import sys

    if len(sys.argv) == 1:
        print("0 arguments.")
    elif len(sys.argv) == 2:
        print("1 argument:")
        print("1: {}".format(sys.argv[1]))

    elif len(sys.argv) > 2:
        print("{} arguments:".format(len(sys.argv) - 1))
        for argc in range(1, len(sys.argv)):
            print("{}: {}".format(argc, sys.argv[argc]))