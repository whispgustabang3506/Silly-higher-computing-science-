# RECAP - UFO
# Original task by Mr Neil, adapted by Mr Simpson

import csv
thisDate = []
country = []
location = []
shape = []
description = []
filePath = 'c:/Users/I.Innes/Silly-higher-computing-science-/Practice assignments/UFO/'

# -------------------------------------------------- DO NOT ALTER -----
def importFile():
    with open(filePath+'ufo_sighting.csv','r') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        for row in reader:
            thisDate.append(row[0])
            country.append(row[1])
            location.append(row[2])
            shape.append(row[5])
            description.append(row[6])
    return thisDate, country, location, shape, description
# -------------------------------------------------- DO NOT ALTER -----

# # CountSightings()
# Count the number of sightings for a specified country.
# IN: country[], specifiedCountry
# OUT: numSightings

# DisplaySightings()
# Display the number of sightings for a specific country.
# IN: specifiedCountry, numSightings
# OUT:

def CountSightings(country, specifiedCountry):
    numSightings = 0
    for index in range(0,len(country)):
        if country[index] == specifiedCountry:
            numSightings = numSightings + 1

    return numSightings
#return takes the local varaibles and passes it back to the main program 
#function count sighting creates an array that serarches through ever occurance where the specified country is named and if it is found the number of occurances for this country will increase 

def DisplaySightings(specifiedCountry, numSightings):
    print(specifiedCountry, numSightings)
    pass
#pass does nothing but lets the program contuine 


#main program 
thisDate, country, location, shape, description = importFile()
specifiedCountry = "England"
numSightings = CountSightings(country, specifiedCountry)
DisplaySightings(specifiedCountry, numSightings)

specifiedCountry = "Scotland"
numSightings = CountSightings(country, specifiedCountry)
DisplaySightings(specifiedCountry, numSightings)

specifiedCountry = "Wales"
numSightings = CountSightings(country, specifiedCountry)
DisplaySightings(specifiedCountry, numSightings)

specifiedCountry = "Northern Ireland"
numSightings = CountSightings(country, specifiedCountry)
DisplaySightings(specifiedCountry, numSightings)