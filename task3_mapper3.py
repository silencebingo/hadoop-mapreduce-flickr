#!/usr/bin/python
import sys

def map5():
    #city \t number \t tagsdetail
    for line in sys.stdin:
        parts = line.strip().split("\t")
        city,number,tagsdetail = parts[0].strip(),parts[1].strip(),parts[2].strip()
        print (number + "\t" + city + "\t" + tagsdetail)

if __name__ == "__main__":
    map5()