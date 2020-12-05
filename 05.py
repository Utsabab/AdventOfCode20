import math


def part1(data):
    inpt = data.split("\n")

    def binarysearch(start, end, c):
        mid = (start + end) / 2
        if c == "F" or c == "L":
            return math.floor(mid)
        else:
            return math.ceil(mid)

    ans = 0
    row = 0
    column = 0
    for i in inpt:
        start = 0
        end = 127
        for j in range(7):
            if i[j] == "F":
                end = binarysearch(start, end, i[j])
                row = end
            else:
                start = binarysearch(start, end, i[j])
                row = start

        start = 0
        end = 7
        for k in range(7,10):
            if i[k] == "L":
                end = binarysearch(start, end, i[k])
                column = end
            else:
                start = binarysearch(start, end, i[k])
                column = start
        ans = max(ans, ((row * 8) + column))

    return ans


def part2(data):
    inpt = data.split("\n")
    seats = []
    def binarysearch(start, end, c):
        mid = (start + end) / 2
        if c == "F" or c == "L":
            return math.floor(mid)
        else:
            return math.ceil(mid)

    ans = 0
    row = 0
    column = 0
    for i in inpt:
        start = 0
        end = 127
        for j in range(7):
            if i[j] == "F":
                end = binarysearch(start, end, i[j])
                row = end
            else:
                start = binarysearch(start, end, i[j])
                row = start

        start = 0
        end = 7
        for k in range(7, 10):
            if i[k] == "L":
                end = binarysearch(start, end, i[k])
                column = end
            else:
                start = binarysearch(start, end, i[k])
                column = start
        seats.append((row * 8) + column)

    seats = sorted(seats)
    for s in range(1,len(seats)):
        if seats[s] - 1 != seats[s-1]:
            return seats[s] - 1

