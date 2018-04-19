#!/usr/bin/python3
import sys
"""This is map1_task1.py"""

def mapper1():
    """select place_id, place_type_id, place_name"""
    for line in sys.stdin:
        parts = line.strip().split("\t")
        # parts = ['place-id', 'woeid', 'latitude', 'longitude', 'place-name', 'place-type-id', 'place-url']
        
        if len(parts) == 7 : 
            place_id,place_type_id, place_name = parts[0].strip(),parts[5].strip(), parts[4].strip()
            print(place_id + "\t" + place_type_id + "\t" + place_name)

if __name__ == "__main__":
    mapper1()

