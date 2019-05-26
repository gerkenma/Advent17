input = open("day8.txt", "r")
registers = {}
m = 0

for line in input:
    print registers
    command = line.split(" ")

    try:
        registers[command[0]]
    except KeyError:
        registers[command[0]] = 0

    try:
        registers[command[4]]
    except KeyError:
        registers[command[4]] = 0

    if (command[5] == ">"):

        if registers[command[4]] > int(command[6]):
            if command[1] == "inc":
                registers[command[0]] += int(command[2])
            else:
                registers[command[0]] -= int(command[2])

    elif (command[5] == "<"):

        if registers[command[4]] < int(command[6]):
            if command[1] == "inc":
                registers[command[0]] += int(command[2])
            else:
                registers[command[0]] -= int(command[2])

    elif (command[5] == ">="):

        if registers[command[4]] >= int(command[6]):
            if command[1] == "inc":
                registers[command[0]] += int(command[2])
            else:
                registers[command[0]] -= int(command[2])

    elif (command[5] == "<="):

        if registers[command[4]] <= int(command[6]):
            if command[1] == "inc":
                registers[command[0]] += int(command[2])
            else:
                registers[command[0]] -= int(command[2])


    elif (command[5] == "=="):

        if registers[command[4]] == int(command[6]):
            if command[1] == "inc":
                registers[command[0]] += int(command[2])
            else:
                registers[command[0]] -= int(command[2])

    elif (command[5] == "!="):

        if registers[command[4]] != int(command[6]):
            if command[1] == "inc":
                registers[command[0]] += int(command[2])
            else:
                registers[command[0]] -= int(command[2])

    else:
        print "Something went wrong."
        break

    if m < registers[max(registers, key=registers.get)]:
        m = registers[max(registers, key=registers.get)]

print registers
print m
