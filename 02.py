import collections

def fixInput(data):
    list_data = data.split("\n")
    return list_data

def part1(data):
    valid = 0
    list_data = fixInput(data)

    for i in list_data:
        curr = i.split(" ")
        minandmax = curr[0].split("-")
        mini = int(minandmax[0])
        maxi = int(minandmax[1])
        tofind = curr[1][0]
        map_count = collections.Counter(curr[2])
        if mini <= map_count[tofind] <= maxi:
            valid += 1
    return valid

def part2(data):
    valid = 0
    list_data = fixInput(data)

    for i in list_data:
        curr = i.split(" ")
        minandmax = curr[0].split("-")
        first = int(minandmax[0])
        second = int(minandmax[1])
        tofind = curr[1][0]
        tocheck = curr[2]
        if tocheck[first-1] == tofind and tocheck[second-1] == tofind:
            continue
        elif tocheck[first-1] != tofind and tocheck[second-1] != tofind:
            continue
        else:
            valid += 1
    return valid