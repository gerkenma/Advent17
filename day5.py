from copy import deepcopy
banks = [11, 11, 13, 7, 0, 15, 5, 5, 4, 4, 1, 1, 7, 1, 15, 11]
infinite = False
maxIndex = None
memory = []

def day5a():
    iterations = 0
    while not infinite:

        for i in range(len(banks)):
            if banks[i] == max(banks):
                maxIndex = i
                break

        value = banks[maxIndex]
        step = maxIndex + 1
        banks[maxIndex] = 0
        while value != 0:
            if step >= len(banks): step -= len(banks)
            banks[step] += 1
            step += 1
            value -= 1

        iterations += 1
        count = 1
        if banks in memory:
            for obj in memory[::-1]:
                if obj == banks:
                    return count
                else:
                    count += 1
            # return iterations
        else: memory.append(deepcopy(banks))


print day5a()