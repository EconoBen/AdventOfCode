import numpy as np

def input(path: str)->list:
    with open(path) as f:
        text = [line.replace("\n","") for line in f.readlines()]
    return text

def tree_count(data:list, xslope:int, yslope:int):
    slope = (xslope, yslope)
    position = (0, 0)
    tree_count = 0

    for index, val in enumerate(data):
        i, j = position[0] + slope[0], position[1] + slope[1]

        if j >= len(val):
            j = j - len(val)

        if i > index:
            continue

        position = (i, j)

        if val[j] == '#':
            tree_count +=1   
    
    return tree_count

def testone(testdata:list, yslope:int, xslope:int):
    return tree_count(test_data, yslope, xslope)

def partone(path:str, xslope:int, yslope:int)->int:
    data = input(path)
    results = tree_count(data, xslope, yslope)
    return results

def testtwo():
    test_slopes = [(1,1), (1,3), (1,5), (1, 7), (2, 1)]
    testresults = []
    for slopes in test_slopes:
        testresults.append(testone(test_data, slopes[0], slopes[1]))
    return np.prod(testresults)

def parttwo(path:str):
    data = input(path)
    slopes = [(1,1), (1,3), (1,5), (1, 7), (2, 1)]
    results = []
    for slopes in slopes:
        results.append(tree_count(data, slopes[0], slopes[1]))
    return np.prod(results)

    
if __name__ == "__main__":
    path = "/Users/blabaschin/Documents/Technical/GitHub/AOC2020/daythree.txt"

    test_data = ["..##.......",
                 "#...#...#..",
                 ".#....#..#.",
                 "..#.#...#.#",
                 ".#...##..#.",
                 "..#.##.....",
                 ".#.#.#....#",
                 ".#........#",
                 "#.##...#...",
                 "#...##....#",
                 ".#..#...#.#"]

    # test part one solution
    testone_results = testone(test_data, 1, 3)
    assert testone_results == 7

    # part one solution
    count = partone(path, 1,3)
    print("solution one:", count)

    # test part two solution
    testtwo_results = testtwo()
    assert testtwo_results == 336

    # part two solution
    counttwo = parttwo(path)
    print("solution two:", counttwo)
