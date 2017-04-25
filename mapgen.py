#Import Google Maps From The Geopy Library
from geopy.geocoders import GoogleV3 as googlemaps
geolocator = googlemaps()

#Read The ‘loc.txt’ File For The Current Location As Coordinates
with open("loc.txt","r") as text_file:
   loc = text_file.read()
#Get The Location As Text Using The Coordinates
location = geolocator.reverse(loc, True)
#Add The Obtained Location's Address To A Reference Variable
addrf = location.address
centrf = loc

#Read The ‘dest.txt’ File For The Destination As Coordinates
with open("dest.txt", "r") as text_file:
   dest = text_file.read()
#Get The Destination As Text Using The Coordinates
location = geolocator.reverse(dest, True)
#Add The Obtained Location's Address To A Reference Variable
destrf = location.address

#Open The ‘mapnew.html’ File And Replace The “start_repl” and “end_repl” Strings
#   with actual address references taken from the text files above.
with open("mapnew.html", "r") as text_file:
   mapgen = text_file.read()

mapgen = mapgen.replace("start_repl", addrf)
mapgen = mapgen.replace("end_repl", destrf)
mapgen = mapgen.replace("centre_repl", centrf)

#Override the ‘mapf.html’ file with the ‘mapnew.html’ file
with open("mapf.html", "w") as text_file:
   text_file.write(mapgen)

#import the subprocess library and call another python file called ‘browser.py’
import subprocess
subprocess.call(['python','browser.py'])
