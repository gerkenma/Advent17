input = open("day9.txt", "r")

garbage = False
open = 0
score = 0
trash = 0

with input as file:
    while True:
        c = file.read(1)

        if (c == "<" and not garbage):
            garbage = True

        elif (c == ">" and garbage):
            garbage = False

        elif (c == "{" and not garbage):
            open += 1

        elif (c == "}" and not garbage):
            score += open
            open -= 1

        elif (c == "!" and garbage):
            file.read(1)

        elif garbage:
            print "Counting as trash:", c
            trash += 1

        if not c:
            print score
            print trash
            break