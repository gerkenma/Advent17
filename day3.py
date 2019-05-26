num = 368078
xmax = 0
ymax = 0
xstep = 0
ystep = 0
dir = True
i = 1

while i < num:
    if dir:

        xmax += 1
        while xstep < xmax:
            xstep += 1
            i += 1
            if (i == num): break

        ymax += 1
        while ystep < ymax:
            ystep += 1
            i += 1
            if (i == num): break

        dir = not dir

    else:

        while xstep > -xmax:
            xstep -= 1
            i += 1
            if (i == num): break

        while ystep > -ymax:
            ystep -= 1
            i += 1
            if (i == num): break

        dir = not dir

print (abs(xstep) + abs(ystep)) - 1

#day3 part b in excel file