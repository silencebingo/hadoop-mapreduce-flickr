#!/usr/bin/python3
import sys

def mapper2():
    """ This mapper selects photos on the filtered location and outputs the photo id, date taken and place url.
    Input format: photo_id \t owner \t tags \t date_taken \t place_id \t accuracy
    Output format: city \t photo_id
    
    """
    place_id_to_city={}
    #place_id,place_type_id, place_url
    with open("part-00000") as f:
        for line in f:
            parts = line.strip().split("\t")
            if len(parts) != 3:
                continue
            place_id,place_type_id, place_name = parts[0].strip(),parts[1].strip(),parts[2].strip()
            city=""
            if place_type_id == '7':
                city = place_name
            elif place_type_id == '22':
                city = place_name.split(",", 1)[-1].strip()
            # city = place_name

            if city != "":
                place_id_to_city[place_id] = city
            # place_id_to_city = {'place_id':city}

    for line in sys.stdin:
            # Clean input and split it
        line = line.strip()
        parts = line.split("\t")

            # Check that the line is of the correct format
        if len(parts) != 6:
            continue

        photo_id, place_id = parts[0].strip(), parts[4].strip()

            # Check that the place_id of the photo is in the filtered location
        if place_id in place_id_to_city:
                # Get the place url given the place id
            photo_city = place_id_to_city[place_id]

                # Output photo_city, photo_id
            print("{}\t{}" .format(photo_city,photo_id))

if __name__ == "__main__":
	mapper2()
