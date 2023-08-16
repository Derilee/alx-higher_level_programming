#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    sum = 0
    for numbers in range(len(sys.argv) - 1):
        sum += int(sys.argv[numbers + 1])
    print("{}".format(sum))
