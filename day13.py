# Part A -- Remake with math instead of simulation
input = open("day13.txt", "r")
layers = {}

for line in input:
    values = line.split(": ")
    layers[int(values[0])] = int(values[1])

severity = 0
for i in layers.keys():
    if i % (2 * layers[i] - 2) == 0:
        severity += i * layers[i]
print severity

# Part B -- magic math stuff that I only kinda understand
delay = 0
caught = True
while caught:
    caught = False
    for i in layers.keys():
        k = layers[i]
        if (i + delay) % (2 * k - 2) == 0:
            caught = True
            delay += 1
            break

print delay


def partAbySimulation():
    input = open("day13.txt", "r")
    length = 99
    layers = [(None, None, None) for i in range(length)]

    for line in input:
        depth = line.split(": ")
        layers[int(depth[0])] = (int(depth[1]), 0, "down")

    severity = 0

    for pos in range(length):
        if layers[pos][1] == 0:
            severity += pos * layers[pos][0]

        for i in range(length):

            depth = layers[i][0]
            layerPos = layers[i][1]
            direction = layers[i][2]

            if direction == layerPos == depth == None:
                pass # Do nothing cause this index is empty

            elif direction == "down" and layerPos < depth-1:
                layerPos += 1

            elif direction == "down" and layerPos == depth-1:
                layerPos -= 1
                direction = "up"

            elif direction == "up" and layerPos > 0:
                layerPos -= 1

            elif direction == "up" and layerPos == 0:
                layerPos += 1
                direction = "down"

            else:
                print "Something has gone wrong."
                exit(-1)

            layers[i] = (depth, layerPos, direction)

    print severity