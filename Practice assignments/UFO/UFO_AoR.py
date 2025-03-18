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
            reader = reader.strip("\n")
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

def findlocation(arrayOfRecords):   #pos junk
    #print(arrayOfRecords)
    output = ""
    position = -1
    specifiedlocation = input("please enter a location")    
    counter = 0 
    found = False
    foundLocation = -1
    while counter<len(arrayOfRecords) and found == False:
        print("*",arrayOfRecords[counter].location,"*", specifiedlocation)
        if arrayOfRecords[counter].location == specifiedlocation:
            found = True
        else:
            counter = counter + 1 
    if found == True:
        position = counter
        
    else:
        output = "toilet"
    return position

def writeToFile(arrayOfRecords, position):   #writing to file 
    with open(filePath+'identified_sighting.txt','w') as writefile:
        if position != -1:
            output = arrayOfRecords[position].thisDate+ " "+ arrayOfRecords[position].shape + " " +arrayOfRecords[position].description
            writefile.write(output) 
        else:
            writefile.write("Sorry loser. There is nothing to write to the file")    
            

#main program 
arrayOfRecords = [entry() for index in range(2200)]
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

position = findlocation(arrayOfRecords) # setting things up 
writeToFile(arrayOfRecords, position)  #setting things up 