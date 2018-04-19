#!/usr/bin/python3
import sys

def read_map_output(file):
    """ Return an iterator for key, value pair extracted from file (sys.stdin).
    Input format:  number \t city
    Output format: city \t number
    """
    for line in file:
        yield line.strip().split("\t", 1)

def reduce2():
    i = 0
    for number,city in read_map_output(sys.stdin):
        i += 1
        if i <= 50:
            print("{}\t{}".format(city.strip(), number))


if __name__ == "__main__":
    reduce2()
