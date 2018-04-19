#!/usr/bin/python3

import sys


def read_map_output(file):
    """ Return an iterator for key, value pair extracted from file (sys.stdin).
    Input format:  key \t value
    Output format: (key, value)
    """
    for line in file:
        yield line.strip().split("\t", 1)

def reduce4():
    for number,detail in read_map_output(sys.stdin):
        parts = detail.strip().split("\t")
        city,tagsdetail = parts[0].strip(),parts[1].strip()

        print(city+"\t"+number+"\t"+tagsdetail)



if __name__ == "__main__":
    reduce4()