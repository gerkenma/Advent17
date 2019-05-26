table = open("day2.txt", "r")
i = 0
rows = []

for line in table:
    rows.append(line.split("\t"))

print rows

for n in rows:
    l = 0
    for i in n:
        n[l] = int(i)
        l += 1

def day2a():
    chksum = 0
    for n in rows:
        chksum += max(n) - min(n)
    print chksum

def day2b():
    chksum = 0
    for n in rows:
        for i in range(len(n)):
            j = i + 1
            while j < (len(n)):
                if n[i]%n[j] == 0:
                    chksum += n[i]/n[j]
                    j = len(n)
                elif n[j]%n[i] == 0:
                    chksum += n[j]/n[i]
                    j = len(n)
                j += 1
    print chksum


day2b()