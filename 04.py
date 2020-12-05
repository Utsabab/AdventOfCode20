def part1(data):
    ans = 0
    count = 0
    tracker = set()
    for ind, i in enumerate(data.split("\n")):
        if not i:
            if len(tracker) == 8 or (len(tracker) == 7 and "cid" not in tracker):
                ans += 1
            count = 0
            tracker = set()
            continue
        temp = i.split(" ")
        for t in temp:
            tracker.add(t.split(":")[0])
        count += len(temp)

    if len(tracker) == 8 or (len(tracker) == 7 and "cid" not in tracker):
        ans += 1
    return ans


def part2(data):

    def checkvalids(tracker):
        hairclr = {'a', 'b', 'c', 'd', 'e', 'f', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9'}
        eyeclr = {"amb", "blu", "brn", "gry", "grn", "hzl", "oth"}
        for k, v in tracker.items():
            if k == "byr":
                if int(v) < 1920 or int(v) > 2002:
                    return False
            if k == "iyr":
                if int(v) < 2010 or int(v) > 2020:
                    return False
            if k == "eyr":
                if int(v) < 2020 or int(v) > 2030:
                    return False
            if k == "hgt":
                if "cm" not in v and "in" not in v:
                    return False
                if v[-2:] == "cm":
                    if int(v[:-2]) < 150 or int(v[:-2]) > 193:
                        return False
                elif v[-2:] == "in":
                    if int(v[:-2]) < 59 or int(v[:-2]) > 76:
                        return False
            if k == "hcl":
                if v[0] != "#" or len(v[1:]) != 6:
                    return False
                for item in v[1:]:
                    if item not in hairclr:
                        return False
            if k == "ecl":
                if v not in eyeclr:
                    return False
            if k == "pid":
                if len(v) != 9 or v.isnumeric() == "False":
                    return False
        return True

    ans = 0
    count = 0
    tracker = {}
    for ind, i in enumerate(data.split("\n")):
        if not i:
            if len(tracker) == 8 or (len(tracker) == 7 and "cid" not in tracker):
                if checkvalids(tracker):
                    ans += 1
            count = 0
            tracker = {}
            continue
        temp = i.split(" ")
        for t in temp:
            k, v = t.split(":")
            tracker[k] = v
        count += len(temp)

    if len(tracker) == 8 or (len(tracker) == 7 and "cid" not in tracker):
        if checkvalids(tracker):
            ans += 1
    return ans
