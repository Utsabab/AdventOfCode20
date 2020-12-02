def fixInput(data):
    list_data = data.split("\n")
    for i, d in enumerate(list_data):
        list_data[i] = int(d)
    return list_data


def part1(data):
    __import__('time').sleep(1)
    # Data is automatically read from 01.txt.txt
    list_data = fixInput(data)
    dict_pairs = set()

    for item in list_data:
        if 2020 - item in dict_pairs:
            return item * (2020 - item)
        else:
            dict_pairs.add(item)


def part2(data):
    list_data = fixInput(data)
    dict_pairs = set()
    for i in list_data:
        for j in list_data:
            if 2020 - i - j in dict_pairs:
                return i * j * (2020 - i - j)
        dict_pairs.add(i)






