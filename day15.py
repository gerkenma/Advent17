def convertToBinary(n):

    binString = ""
    while n != 0:
        binString = str(n%2) + binString
        n /= 2

    while len(binString) <= 40:
        binString = "0" + binString

    return binString


a = 516
b = 190
count = 0

for i in range(5000000):
    aCriteria = False
    bCriteria = False

    while not aCriteria:
        a *= 16807
        a %= 2147483647

        if a % 4 == 0:
            aCriteria = True

    while not bCriteria:
        b *= 48271
        b %= 2147483647

        if b % 8 == 0:
            bCriteria = True

    binA = convertToBinary(a)
    binB = convertToBinary(b)

    if binA[-16:] == binB[-16:]:
        count += 1

    if i % 1000 == 0: print i

print count