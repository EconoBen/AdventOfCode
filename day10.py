from typing import List, DefaultDict
from collections import defaultdict
import itertools

def input(path:str)-> List[str]:
    with open(path) as f:
        raw = f.read()
    textcurr_list = [int(string) for string in raw.split("\n")]
    return textcurr_list


def test_plugs(effective_rate:int, intcurr_list:List[int]):
    diff_dict = defaultdict(int)
    max_val = [max(intcurr_list) + 3]
    for jolt in sorted(intcurr_list+max_val):
        diff = jolt - effective_rate
        diff_dict[diff] += 1
        effective_rate = jolt
    return diff_dict

def count_paths(int_list:List[int]):
    int_list.append(0)
    int_list.append(max(int_list) + 3)
    
    output = int_list[-1]

    # num_ways[i] is the number of ways to get to i
    num_ways = [0] * (output +1)
    num_ways[0] = 1

    if 1 in int_list:
        num_ways[1] = 1

    if 2 in int_list and 1 in int_list:
        num_ways[2] = 2
    elif 2 in int_list:
        num_ways[2] = 1

    for n in range(3, output + 1):
        if n not in int_list:
            continue
        
        num_ways[n] = num_ways[n-3] + num_ways[n-2] + num_ways[n-1]
    return num_ways[output]

if __name__ == "__main__":

    # test one text
    testone_text = input('/Users/blabaschin/Documents/Technical/GitHub/AOC2020/day10testone.txt')

    # test one
    testone_result = test_plugs(0, testone_text)
    assert (testone_result) == {1: 7, 3: 5}

    # test two text
    testtwo_text = input('/Users/blabaschin/Documents/Technical/GitHub/AOC2020/day10testtwo.txt')

    # test two
    testone_result = test_plugs(0, testtwo_text)
    assert (testone_result) == {1: 22, 3: 10}

     # part one text
    partone_text = input('/Users/blabaschin/Documents/Technical/GitHub/AOC2020/day10.txt')

    # part one
    partone_result = test_plugs(0, partone_text)
    print(partone_result[1]* partone_result[3])

    # test three
    starting_index = [0,1]

    assert count_paths(testone_text) == 8
    assert count_paths(testtwo_text) == 19208

    print(count_paths(partone_text))
    
    