#!/usr/bin/python3
import sys


def map4():
    #city,photonumber
    top_dict = {}
    with open("part-00000") as f:
        for line in f:
            parts = line.strip().split("\t")
            city, number = parts[0].strip(),parts[1].strip()
            top_dict[city] = number

    for line in sys.stdin:
        # Clean input and split it
        parts = line.strip().split("\t")

        # Check that the line is of the correct format
        if len(parts) != 3:
        # The line comes from map4(city,year,tags)
            continue
        city,year, tags = parts[0].strip(),parts[1].strip(), parts[2].strip()
        #output city,number,date,tags
        if city in top_dict:
            print (city + "\t" + top_dict[city] + "\t" + year + "\t" + tags)



if __name__ == "__main__":
    map4()



