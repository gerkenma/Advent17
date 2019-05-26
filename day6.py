tower = open("day6.txt", "r")
import re

structure = {}
for line in tower:
    subtower = line.split(" ")

    key = subtower[0]
    weight = int(re.findall('[0-9]+', subtower[1])[0])
    children = subtower[3:]

    cleanChildren = []
    for node in children:
        cleanChildren += re.findall('[a-z]+', node)

    structure[key] = [weight] + cleanChildren

weights = {}

def findTowerWeight(parent):

    childWeights = []
    weight = structure[parent][0]
    i = 0

    if len(structure[parent]) == 1:
        weight = structure[parent][0]

    else:
        for child in structure[parent][1:]:
            childWeights.append((child, findTowerWeight(child)))
            weight += childWeights[len(childWeights) - 1][1]

    weights[parent] = childWeights
    return weight

print findTowerWeight("vtzay")
print weights["vtzay"]
print weights["qawlwzi"]
print weights["jfrda"]
print weights["lnpuarm"]

