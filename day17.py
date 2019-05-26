from collections import deque

circBuffer = deque([0])
step = 304

for i in range(1, 50000001):
	circBuffer.rotate(-step)
	circBuffer.append(i)
	if i % 1000000 == 0: print i

print circBuffer[list(circBuffer).index(0) + 1]