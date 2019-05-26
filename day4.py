input = open("day4.txt", "r")

def day4a():
    count = 0
    for line in input:
        line = line.rstrip()
        passphrase = line.split(" ")
        if len(passphrase) == len(set(passphrase)):
            count += 1
    return count


def day4b():
    count = 0
    for line in input:
        line = line.rstrip()
        passphrase = line.split(" ")

        print passphrase
        for i in range(len(passphrase)):
            passphrase[i] = ''.join(sorted(passphrase[i]))

        print passphrase
        if len(passphrase) == len(set(passphrase)):
            count += 1

    return count

print day4b()