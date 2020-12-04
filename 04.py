# def fixInput(data):



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



    # print(neww)

# def part2(data):