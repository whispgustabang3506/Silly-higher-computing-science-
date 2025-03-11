# RECAP - UFO
# Original task by Mr Neil, adapted by Mr Simpson

from dataclasses import dataclass

@dataclass
class entry():
    thisDate : str = ""
    country : str = ""
    location : str = ""
    shape : str = ""
    description : str = ""

filePath = 'c:/Users/I.Innes/Silly-higher-computing-science-/Practice assignments/UFO/'

# -------------------------------------------------- DO NOT ALTER -----
def importFile(arrayOfRecords):
    with open(filePath+'ufo_sighting.txt','r') as file:
        reader = file.readline()
        index = 0
        while reader != "":
            reader = reader.strip()
            row = reader.split(',')
            arrayOfRecords[index].thisDate = row[0]
            arrayOfRecords[index].country = row[1]
            arrayOfRecords[index].location = row[2]
            arrayOfRecords[index].shape = row[5]
            arrayOfRecords[index].description = row[6]
            index = index + 1
            reader = file.readline()
    return arrayOfRecords
# -------------------------------------------------- DO NOT ALTER -----

# # CountSightings()
# Count the number of sightings for a specified country.
# IN: country[], specifiedCountry
# OUT: numSightings

# DisplaySightings()
# Display the number of sightings for a specific country.
# IN: specifiedCountry, numSightings
# OUT:

def CountSightings(arrayOfRecords, specifiedCountry):
    numSightings = 0
    for index in range(0,len(arrayOfRecords)):
        if arrayOfRecords[index].country == specifiedCountry:
            numSightings = numSightings + 1

    return numSightings
#return takes the local varaibles and passes it back to the main program 
#function count sighting creates an array that serarches through ever occurance where the specified country is named and if it is found the number of occurances for this country will increase 

def DisplaySightings(specifiedCountry, numSightings):
    print(specifiedCountry, numSightings)
    pass
#pass does nothing but lets the program contuine 

#CountYearSightings()
#Count the sightings each year.
#IN: thisDate [ ]
#OUT:

def CountYearSightings(arrayOfRecords):
    yearsightings = 0
    for index in range(0, len(arrayOfRecords)-1):
        currDate = arrayOfRecords[index].thisDate[6:10]
        nextDate = arrayOfRecords[index+1].thisDate[6:10]
        if currDate == nextDate:
            yearsightings = yearsightings + 1
        else:
            print(currDate, yearsightings)
            yearsightings = 0

#FindSightingsByLocation() 
#Count the sightings each year. 
#IN: location [ ], thisDate [ ], shape [ ], description [ ] 
#OUT:

def findlocation(arrayOfRecords):
    specifiedlocation = input("please enter a location")    
    counter = 0 
    found = False
    foundLocation = -1
    while counter<len(arrayOfRecords) and found == False:
        if arrayOfRecords[counter].location == specifiedlocation:
            found = True
            counter = counter
    else:
        counter = counter + 1 
    if found == True:
        print(arrayOfRecords[counter].thisDate, arrayOfRecords[counter].shape, arrayOfRecords[counter].description)
    else:
        print("toilet")
        

            
    
        

#main program 
arrayOfRecords = [entry() for index in range(5000)]
arrayOfRecords = importFile(arrayOfRecords)

specifiedCountry = "England"
numSightings = CountSightings(arrayOfRecords, specifiedCountry)
DisplaySightings(specifiedCountry, numSightings)

specifiedCountry = "Scotland"
numSightings = CountSightings(arrayOfRecords, specifiedCountry)
DisplaySightings(specifiedCountry, numSightings)

specifiedCountry = "Wales"
numSightings = CountSightings(arrayOfRecords, specifiedCountry)
DisplaySightings(specifiedCountry, numSightings)

specifiedCountry = "Northern Ireland"
numSightings = CountSightings(arrayOfRecords, specifiedCountry)
DisplaySightings(specifiedCountry, numSightings)

specifiedyear = arrayOfRecords[0].thisDate
yearsightings = CountYearSightings(arrayOfRecords)

findlocation(arrayOfRecords) 