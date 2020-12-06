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

# def part2(data):
