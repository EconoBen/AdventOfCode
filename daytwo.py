import numpy as np
from collections import Counter

def input(text:str)->np.array:
    text = np.loadtxt(text, dtype=str)
    return text

def partone_testcases()->int:
    arrays = [['1-3', 'a:', 'abcde'],
             ['1-3', 'b:', 'cdefg'],
             ['2-9', 'c:', 'ccccccccc']]
    valid_counter = 0
    for array in arrays:
        counter_dict = Counter(array[-1])
        lowerb, upperb = list(map(int, array[0].split("-")))
        condition = counter_dict[array[1].replace(":","")]
        if (condition >= lowerb) & (condition <= upperb):
            valid_counter += 1
        else:
            pass
    return valid_counter

def part_one(input:list)->int:
    
    valid_counter = 0
    for array in data:
        counter_dict = Counter(array[-1])
        lowerb, upperb = list(map(int,array[0].split("-")))
        condition = counter_dict[array[1].replace(":","")]
        if (condition >= lowerb) & (condition <= upperb):
            valid_counter += 1
        else:
            pass
    return valid_counter


def parttwo_testcases()->int:
    arrays = [['1-3', 'a:', 'abcde'],
             ['1-3', 'b:', 'cdefg'],
             ['2-9', 'c:', 'ccccccccc']]
    valid_counter = 0
    for array in arrays:
        pos_dict = {index+1: letter for index, letter in enumerate(array[-1])}
        lowerb, upperb = list(map(int, array[0].split("-")))
        condition = array[1].replace(":","")
        if (condition == pos_dict[lowerb]) & (condition != pos_dict[upperb]):
            valid_counter += 1
        else:
            pass
    return valid_counter

def part_two(input:list)->int:
    
    valid_counter = 0
    for array in input:
        pos_dict = {index: letter for index, letter in enumerate(array[-1],1)}
        lowerb, upperb = list(map(int, array[0].split("-")))
        condition = array[1].replace(":","")
        if (condition == pos_dict[lowerb]) & (condition != pos_dict[upperb]):
            valid_counter += 1
        elif (condition != pos_dict[lowerb]) & (condition == pos_dict[upperb]):
            valid_counter += 1
        else:
            pass
    return valid_counter

if __name__ == "__main__":
    data = input("/Users/blabaschin/Documents/Technical/GitHub/AOC2020/daytwo.txt")
    
    # part one
    testcaseone = partone_testcases()
    assert testcaseone == 2

    print(f"Part one has {part_one(data)} valid cases.")

    # part two
    testcasetwo = parttwo_testcases()
    assert testcasetwo == 1

    print(f"Part two has {part_two(data)} valid cases.")
