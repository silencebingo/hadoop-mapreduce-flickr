#!/usr/bin/python3
import sys

def map3():
    for line in sys.stdin:
        parts = line.split("\t")
        number,city = parts[1].strip(),parts[0].strip()
        print(number+"\t"+city)


if __name__ == "__main__":
    map3()
