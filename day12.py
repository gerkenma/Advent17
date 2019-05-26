table = {}
# input = open("day12.txt", "r")
input = open("day12b.txt", "r")


def buildTable():
    for line in input:
        relationship = line.split(" ")
        relationship[0] = int(relationship[0])
        for i in range(2, len(relationship)): relationship[i] = int(relationship[i].rstrip(",\n"))

        table[relationship[0]] = relationship[2:]


def explore(num, past):
    if num not in connected:
        if num == 0 or 0 in table[num]:
            print num, "is connected directly."
            connected[num] = True

        else:

            toExplore = []
            for val in table[num]:
                if val not in past:
                    toExplore.append(val)

            childConnect = []
            for val in toExplore:
                if val in connected and connected[val]:
                        print num, "is connected to", val, "which is connected to zero."
                        connected[num] = True
                        return

                elif val in connected:
                    print val, "has been previously found to not be connected."
                    childConnect.append(False)

                else:
                    explore(val, past + [val])
                    childConnect.append(connected[val])
                    print val, "has been found to be", connected[val]

            if True in childConnect:
                print "Some child of", num, "is connected."
                connected[num] = True

            else:
                print "No child of", num, "is connected."
                connected[num] = False

    else:
        print "Already evaluated", num


buildTable()
connected = {}
print table

for num in table:
    print "Evaluating", num
    explore(num, [num])

total = 0
print connected

for key in connected:
    if connected[key]: total += 1

print total