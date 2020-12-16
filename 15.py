def part1(data):
    stck = data.split(",")
    for i in range(len(stck)):
        stck[i] = int(stck[i])

    dict_nums = {}
    for ind, num in enumerate(stck):
        dict_nums[num] = [ind+1,ind+1,1]

    for i in range(len(stck)+1, 2021):
        curr = stck[-1]
        if dict_nums[curr][2] == 1:
            stck.append(0)
            if 0 in dict_nums:
                dict_nums[0][2] += 1
                dict_nums[0][0] = dict_nums[0][1]
                dict_nums[0][1] = i
            else:
                dict_nums[0] = [i,i,1]
        else:
            temp = dict_nums[curr][1] - dict_nums[curr][0]
            stck.append(temp)
            if temp in dict_nums:
                dict_nums[temp][0] = dict_nums[temp][1]
                dict_nums[temp][1] = i
                dict_nums[temp][2] += 1
            else:
                dict_nums[temp] = [i,i,1]

    return stck[-1]

# def part2(data):

