def aoc_p1():
    with open("/Users/blabaschin/Documents/Technical/GitHub/AOC2020/dayonep1.txt") as f:
        lines = f.readlines()
        lines = {index: int(line.replace("\n","")) for index, line in enumerate(lines)}
        for index, value in lines.items():
            target = 2020 - value
            if target in lines.values():
                return print(value * target)
aoc_p1()

def aoc_p2():
     with open("/Users/blabaschin/Documents/Technical/GitHub/AOC2020/dayonep1.txt") as f:
        lines = f.readlines()
        lines = {index: int(line.replace("\n","")) for index, line in enumerate(lines)}
        for index, value in lines.items():
            target = 2020 - value
            new_dict = lines.copy()
            del new_dict[index]
            for new_index, new_value in new_dict.items():
                new_target = target - new_value
                if new_target in new_dict.values():
                    return print(value *  new_value * new_target)
aoc_p2()
