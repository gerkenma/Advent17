import re

data = open('day12.txt').readlines()
data = [re.split(', | ', i.strip()) for i in data]

def get_connected(n):
    global group
    cur = data[n]
    new_num = [int(j) for j in data[n][2:]]
    for i in new_num:
        if not(i in group):
            group += [i]
            get_connected(i)

#keep track of whether or not a number belongs to a group
connections = [-1]*len(data)
for i in range(len(data)):
    if not(connections[i] == -1): #skip if number already part of group
        continue
    group = [i]
    get_connected(i)
    for j in group: connections[j] = i

print 'Part 1: ' + str(connections.count(0))
print 'Part 2: ' + str(len(set(connections)))