import json
from pprint import pprint
import gmplot


#Find and filters all airport in a country based on its 2 letter symbol
def findAirportInCountires(country):
    with open('airports.json') as f: #File from https://github.com/mwgg/Airports
        data = json.load(f)
        foundEntries = 0

        results = []
        for i in data:
            if data[i]["country"] in country and data[i]["iata"] != "":
                results.append(data[i])
                foundEntries += 1

        print "Found: " + str(foundEntries)
    return results

#Extract iato (needed to search flights)
def extract_iata(airportResults):
    iataArr = []
    for i in airportResults:
        iata = i["iata"]
        if iata != "":
            iataArr.append(iata)
    return iataArr

#Draw markers on map where an airport is located based on lat, lon
def drawAirports_lat_lon(airportResults):
    foundFirst = False
    for i in airportResults:
        if foundFirst is not True:
            zz =  i
            gmap = gmplot.GoogleMapPlotter(i["lat"], i["lon"], 5)
            foundFirst = True
        hidden_gem_lat, hidden_gem_lon = i["lat"],i["lon"]
        gmap.marker(hidden_gem_lat, hidden_gem_lon, 'cornflowerblue')
    gmap.draw("{}_Airports.html".format(i["country"]))

##########################################################################
#Main
res = findAirportInCountires("DE") #Country 2 letter code translation #https://www.worldatlas.com/aatlas/ctycodes.htm
drawAirports_lat_lon(res)
iata =  extract_iata(res)







