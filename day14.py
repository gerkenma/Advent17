from day10 import hashString

import binascii
from day10 import hashString

# Only completed Part A
hex = {}
hex["0"] = "0000"
hex["1"] = "0001"
hex["2"] = "0010"
hex["3"] = "0011"
hex["4"] = "0100"
hex["5"] = "0101"
hex["6"] = "0110"
hex["7"] = "0111"
hex["8"] = "1000"
hex["9"] = "1001"
hex["a"] = "1010"
hex["b"] = "1011"
hex["c"] = "1100"
hex["d"] = "1101"
hex["e"] = "1110"
hex["f"] = "1111"

key = "hwlqcszp"
rows = [hashString(key+"-"+str(i)) for i in range(128)]
print rows
ones = 0
zeroes = 0

for entry in rows:
    row = ""
    for char in entry:
        row += hex[char]
    ones += row.count("1")
    zeroes += row.count("0")
    print row

print ones


def day14stolen():
    data = 'hwlqcszp'
    rows = []

    n = 0
    for i in xrange(128):
        v = hashString('%s-%d' % (data, i))
        print '%s-%d' % (data, i)
        v = '{:0128b}'.format(int(v, 16))
        print '{:0128b}'.format(int(v, 16))
        n += sum(map(int, v))
        print sum(map(int, v))
        rows.append(map(int, v))

    print n

    seen = set()
    n = 0
    def dfs(i, j):
        if ((i, j)) in seen:
            return
        if not rows[i][j]:
            return
        seen.add((i, j))
        if i > 0:
            dfs(i-1, j)
        if j > 0:
            dfs(i, j-1)
        if i < 127:
            dfs(i+1, j)
        if j < 127:
            dfs(i, j+1)

    for i in xrange(128):
        for j in xrange(128):
            if (i,j) in seen:
                continue
            if not rows[i][j]:
                continue
            n += 1
            dfs(i, j)

    print n