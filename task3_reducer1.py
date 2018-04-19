#!/usr/bin/python3

import sys
import collections

def read_map_output(file):
    """ Return an iterator for key, value pair extracted from file (sys.stdin).
    Input format:  key \t value
    Output format: (key, value)
    """
    for line in file:
        yield line.strip().split("\t", 1)


def reduce4():
    data = read_map_output(sys.stdin)
    #input city,number,year,tags
    tag_dict = {}
    current_city = ""
    locality = []
    for city, detail in data:
        parts = detail.strip().split("\t")
        number,year,tags = parts[0].strip(),parts[1].strip(),parts[2].strip()
        #filter       
        
        if current_city != city:
            tag_dict[city] = [number,{}]
            current_city = city
            parents = city.split(",")
            parents = [item.strip() for item in parents]
            locality = [item.lower() for item in parents]

        photo_tags = tags.split()
        if current_city in tag_dict:
            locality.append(year)
            
            for tag in photo_tags:
                if  tag not in locality:
                    tag_dict[city][1][tag.strip()] = tag_dict[city][1].get(tag.strip(),0) + 1

            locality.pop()

    for city,detail in tag_dict.items():
        d = collections.Counter(detail[1])
        tag_output = ""
        for tag,value in d.most_common(10):
            tag_output += " (" + tag + ":" + str(value) + ")"
        print (city + "\t" + detail[0] + "\t" + tag_output)

    

if __name__ == "__main__":
    reduce4()

        


        