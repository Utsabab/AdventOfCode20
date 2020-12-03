def fixInput(data):
    list_data = data.split("\n")
    tomult = ((len(list_data) * 7) // len(list_data[0])) + len(list_data[0])
    for i in range(len(list_data)):
        temp = list_data[i]
        for j in range(tomult):
            list_data[i] = list_data[i] + temp
    return list_data

def part1(data):
    list_data = fixInput(data)

    l = len(list_data[0])
    index = 0
    trees = 0
    for ind,item in enumerate(list_data):
        if ind == 0:
            continue

        if item[index+3] == "#":
            trees += 1
        index += 3

    return trees

def part2(data):
    list_data = fixInput(data)
    l = len(list_data[0])
    ans = 1

    def findtrees(right, down):
        trees = 0
        d = down
        r = 0
        for ind, item in enumerate(list_data):
            if ind == d:
                if item[r+right] == "#":
                    trees += 1
                d += down
                r += right
        return trees

    ans *= findtrees(1, 1)
    ans *= findtrees(3, 1)
    ans *= findtrees(5, 1)
    ans *= findtrees(7, 1)
    ans *= findtrees(1, 2)
    return ans