# Part A
#lengths = input.readline()

def hashString(lengths):
    # Part B
    #lengths = '225,171,131,2,35,5,0,13,1,246,54,97,255,98,254,110'
    ascii = []

    # Part A
    #for i in range(len(lengths)): lengths[i] = int(lengths[i])

    #Part B
    for i in range(len(lengths)): ascii.append(ord(lengths[i]))
    ascii += [17, 31, 73, 47, 23]

    list = range(256)
    startP = 0
    endP = lengths[0]
    skipLength = 0
    partA = 0

    for q in range(64):
        for num in ascii:

            if num > len(list):
                print "Invalid."
                break

            if num > 0:
                endP = startP + num
                if endP >= len(list): endP %= len(list)

                if startP < endP:
                    list[startP:endP] = reversed(list[startP:endP])

                else:
                    endRev = list[startP:]
                    beginRev = list[:endP]
                    rev = endRev + beginRev
                    rev[:] = reversed(rev)

                    i = startP
                    for n in rev:
                        if i >= len(list): i %= len(list)
                        list[i] = n
                        i += 1

            startP += num
            startP += skipLength
            if startP >= len(list): startP %= len(list)

            skipLength += 1

    denseHash = []

    for i in range(16):
        value = list[16 * i]
        for j in range(1, 16):
            value ^= list[16 * i + j]

        denseHash.append(value)

    hexString = ""
    for num in denseHash:
        v = hex(num)[2:]
        if len(v) != 2:
            v = "0" + v
        hexString += v

    return hexString
    # print "Part B: ", hexString