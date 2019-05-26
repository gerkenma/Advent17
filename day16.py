def spin(seq, cmd):
	seq = seq[-int(cmd[1:]):] + seq[:-int(cmd[1:])]
	return seq


def exchange(seq, cmd):
	cmd = cmd.split("/")
	numA = int(cmd[0][1:])
	numB = int(cmd[1])
	smol = min(numA, numB)
	big = max(numA, numB)
	a = seq[smol]
	b = seq[big]

	return seq[:smol] + b + seq[smol+1:big] + a + seq[big+1:]


def partner(seq, cmd):
	cmd = cmd.split("/")
	progA = cmd[0][1:]
	progB = cmd[1]

	i = 0
	aPos = None
	bPos = None

	for c in seq:
		if c == progA:
			aPos = i

		elif c == progB:
			bPos = i
		i += 1

	if aPos > bPos:
		temp = aPos
		aPos = bPos
		bPos = temp
		temp = progA
		progA = progB
		progB = temp

	return seq[:aPos] + progB + seq[aPos+1:bPos] + progA + seq[bPos+1:]



input = open("day16.txt", "r")
dance = input.read().split(",")
programs = "abcdefghijklmnop"
# i = 0
seen = []

for i in range(1000000000):
	for move in dance:
		#print "Programs at", programs, "with move", move
		if move[0] == "s":
			programs = spin(programs, move)
		elif move[0] == "x":
			programs = exchange(programs, move)
		elif move[0] == "p":
			programs = partner(programs, move)

	if programs not in seen:
		seen.append(programs)
		if (i % 10000 == 0):
			print "On dance", i

	else:
		break

#Part A
print programs
#Part B
print seen[1000000000 % len(seen) - 1]


