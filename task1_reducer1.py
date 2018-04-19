#!/usr/bin/python3
import sys


def read_map_output(file):
    """ 
    Return an iterator for key, value pair extracted from file (sys.stdin).
    Input format:  key \t value
    Output format: (key, value)
    """
    for line in file:
        yield line.strip().split("\t", 1)

def reduce1():
    """ This reducer perform reduce side join
        Input format: photo_city \t photo_id \t tags
        Output format: cityname \t number of photo
    """
    current_city = ""
    photo_count = 0

    for city,photo_id in read_map_output(sys.stdin):
        # Check if the city read is the same as the city currently being processed
        if current_city != city:
            if current_city != "":
                print("{}\t{}".format(current_city, str(photo_count)))

            current_city = city
            photo_count = 0
        photo_count += 1

    #the last city
    if current_city != "":
        print("{}\t{}" .format(current_city, str(photo_count)))


if __name__ == "__main__":
    reduce1()

