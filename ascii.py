import pywhatkit 
import sys

#after the python3 ascii.py [1] position will be image location
image_location = sys.argv[1]

#python3 ascii.py[2] file name without extension test
image_out_file = sys.argv[2]

pywhatkit.image_to_ascii_art(image_location, image_out_file)
