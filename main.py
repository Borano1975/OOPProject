import Classes
import os.path
import re
import operator
import random

def houseGeneration(num):
    monthlyCare = random.randint(0, 1200)
    if monthlyCare < 500:
        monthlyCare = 0
    return ("House {}, Street {}, {}, {}, {}\n".format(num + 1,
                                                       num + 1,
                                                       random.randint(40000, 90000),
                                                       random.randint(24, 96),
                                                       monthlyCare))


filename = "houses"
file = None  # string saving lines
all_lines = []  # list of saved lines
lines_read = 0  # number of lines saved(1 less because starts from 0)
myAirBNB = {}  # list of AirBNB houses objects to be created.
myLease = {}  # list of leasing houses objects to be created.
houseNumber = 6
leaseHouseNumber = 0
airBNBHouseNumber = 0
f = open(filename + ".txt", "w")
for i in range(houseNumber):
    f.write(houseGeneration(i))
f.close()

if os.path.isfile(filename + ".txt"):
    with open(filename + '.txt') as file:
        for line in file:
            # Assigning each line to all_lines and
            # stripping the file from '\n' chars at the end of each line.
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
            # create lease object with house strips
            myLease[leaseHouseNumber] = Classes.Lease(house[1].strip(),
                                                      house[2].strip(),
                                                      float(house[3].strip()),
                                                      float(house[4].strip()),
                                                      float(house[5].strip()))
            leaseHouseNumber += 1
        else:
            # create airbnb objects with house strips.
            myAirBNB[airBNBHouseNumber] = Classes.AirBNB(house[1].strip(),
                                                         house[2].strip(),
                                                         float(house[3].strip()),
                                                         float(house[4].strip()),
                                                         float(house[5].strip()))
            airBNBHouseNumber += 1
            pass

    else:
        print("You encountered some mistake in separation of each line.")

file.close()
# NOW WE HAVE TO CALCULATE THE MONTHLY EARNING OF EACH HOUSE, whether that is leasing or airbnb.
# and also the total earning from each house.
# We could've done this from the above loop as well, just did not want it to be cluttered.

def getEarnings(myLeaseC, myAirBNBC):
    earnings = {}
    for n in range(len(myLeaseC)):
        # print("Monthly Earnings of house: \" {} \" are : {} ". format(myLease[n].getName(), myLease[n].getQuota()))
        earnings[n] = myLeaseC[n].getQuota()
    for i in range(len(myAirBNBC)):
        # print("Monthly Earnings of house: \" {} \" are : {} ".format(myAirBNB[n].getName(), myAirBNB[n].getQuota()))
        earnings[len(myLeaseC) + i] = myAirBNBC[i].getQuota()
    return earnings

earnings = getEarnings(myLease, myAirBNB)
print(earnings)

def findTotalEarnings(earning_list):
    total = 0
    for x in earning_list:
        total += earning_list[x]
    return int(total)


# Since sort does not work on dictionaries, neither do operands like more or less;
# I have created a method which receives the dictionary,(key: value) in our case;
# That sorts a list of tuples from the second value of earnings dict:
print(earnings)

def findHighestEarning(earnings_list):
    sorted_earnings = sorted(earnings_list.items(), key=operator.itemgetter(1))
    return int(sorted_earnings[len(sorted_earnings) - 1][1])

def findLowestEarning(earnings_list):
    sorted_earnings = sorted(earnings_list.items(), key=operator.itemgetter(1))
    return int(sorted_earnings[0][1])


print("Total earnings: {}".format(findTotalEarnings(earnings)))
print("Highest earning house: {}".format(findHighestEarning(earnings)))
print("Lowest earning house: {}".format(findLowestEarning(earnings)))
