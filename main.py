import Classes
import os.path
import re

filename = "houses"
file = None #string saving lines
all_lines = [] #list of saved lines
lines_read = 0 #number of lines saved(1 less because starts from 0)
myAirBNB = {} #list of AirBNB houses objects to be created.
myLease = {} #list of leasing houses objects to be created.
leaseHouseNumber = 0
airBNBHouseNumber = 0
if os.path.isfile(filename + ".txt"):
    with open(filename + '.txt') as file:
        for line in file:
            #Assigning each line to all_lines and
            #stripping the file from '\n' chars at the end of each line.
            all_lines.append(line[:-1])
            lines_read += 1


"""
The following code is going to:
Check each element where the generated object string is stored(lines of text)
defining the regular expression we're going to compile
Then iterating for each element in all_lines:
Using regular expression to separate the line into strips,(separator is comma)
adding an if else block to check if separation goes well
WE KEEP IN MIND THAT IF MONTHLYCARE is 0 then the house is supposed to be a lease
otherwise, the house is supposed to be an AIRBNB
(Logic behind that is that leasing does not require the owner to go clean the house.)

We create another if else block
if the monthlypayment is 0, create a lease object with the previously stripped string.
else, create an AirBNB object with the previously stripped string.

This is going to happen until the end of list containing all lines.
"""
pattern = re.compile('^([A-Za-z0-9 ]+),([A-Za-z0-9 ]+),([0-9 ]+),([0-9 ]+),([0-9 ]+)$')
for n in range(len(all_lines)):
    house = pattern.search(all_lines[n])
    if house:
        if house[5].strip() == '0':
            #create lease object with house strips
            myLease[leaseHouseNumber] = Classes.Lease(house[1].strip(),
                                                      house[2].strip(),
                                                      float(house[3].strip()),
                                                      float(house[4].strip()),
                                                      float(house[5].strip()))
            leaseHouseNumber += 1
        else:
            #create airbnb objects with house strips.
            myAirBNB[airBNBHouseNumber] = Classes.AirBNB(house[1].strip(),
                                                         house[2].strip(),
                                                         float(house[3].strip()),
                                                         float(house[4].strip()),
                                                         float(house[5].strip()))
            airBNBHouseNumber += 1
            pass

    else:
        print("You encountered some mistake in separation of each line.")

#NOW WE HAVE TO CALCULATE THE MONTHLY EARNING OF EACH HOUSE, whether that is leasing or airbnb.
#and also the total earning from each house.
#We could've done this from the above loop as well, just did not want it to be cluttered.
totalEarning = 0
for n in range(len(myLease)):
    #print("Monthly Earnings of house: \" {} \" are : {} ". format(myLease[n].getName(), myLease[n].getQuota()))
    totalEarning += myLease[n].getQuota()
for n in range(len(myAirBNB)):
    #print("Monthly Earnings of house: \" {} \" are : {} ".format(myAirBNB[n].getName(), myAirBNB[n].getQuota()))
    totalEarning += myAirBNB[n].getQuota()


print("Total Monthly Earnings are: " + str(totalEarning))

#sort algorithm here:
