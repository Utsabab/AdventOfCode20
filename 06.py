import collections


def part1(data):
    ans = 0
    inpt = data.split("\n")
    l = len(inpt) - 1
    unique = set()

    for i in range(len(inpt)):
        if i == l:
            for j in inpt[i]:
                unique.add(j)
            ans += len(unique)
        if not inpt[i]:
            ans += len(unique)
            unique = set()
            continue
        for j in inpt[i]:
            unique.add(j)
    return ans


def part2(data):
    inpt = data.split("\n")
    dict_record = collections.defaultdict(int)
    count = 0
    l = 0

    for i in range(len(inpt)):
        if not inpt[i]:
            for k, v in dict_record.items():
                if v == i - l:
                    count += 1
            dict_record = collections.defaultdict(int)
            l = i + 1
        for j in inpt[i]:
            dict_record[j] += 1

    for k, v in dict_record.items():
        if v == i + 1 - l:
            count += 1
    return count
