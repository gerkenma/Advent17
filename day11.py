x = 0
y = 0
maxV = 0
input = open("day11.txt", "r").readline().rstrip()
directions = input.split(",")

# Turned hexagonal grid into traditional grid
# NW | N |___
# SW |___| NE
# ___| S | SE


for step in directions:
    if step == "n":
        y += 1

    elif step == "ne":
        x += 1

    elif step == "nw":
        y += 1
        x -= 1

    elif step == "s":
        y -= 1

    elif step == "se":
        y -= 1
        x += 1

    elif step == "sw":
        x -= 1

    else:
        print "There's been a problem:", step
        break

    if (abs(x) + abs(y) + abs(x+y))/2 > maxV: maxV = (abs(x) + abs(y) + abs(x+y))/2

print "Part A:", (abs(x) + abs(y) + abs(x+y))/2
print "Part B:", maxV