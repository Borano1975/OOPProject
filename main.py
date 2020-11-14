import Class
import os.path
import re

filename = "houses"
file = None #string saving lines
all_lines = [] #list of saved lines
lines_read = 0 #number of lines saved(1 less because starts from 0)

if os.path.isfile(filename + ".txt"):
    with open(filename + '.txt') as file:
        for line in file:
            #Assigning each line to all_lines and
            #stripping the file from '\n' chars at the end of each line.
            all_lines.append(line[:-1])
            lines_read += 1

pattern = re.compile('^([A-Za-z0-9 ]+),([A-Za-z0-9 ]+),([0-9 ]+),([0-9 ]+),([0-9 ]+)$')
for n in range(len(all_lines)):
    house = pattern.search(all_lines[n])
    if house:
        if int(house[5].strip()) == 0:
            #create lease object with house strips
            print("lease house:")
            pass
        else:
            #create airbnb objects with house strips.
            print("airbnb house:")
            pass
        #dont forget
        print(house[1].strip(), house[2].strip(), house[3].strip(), house[4].strip(), house[5].strip())
    else:
        print("no match")
