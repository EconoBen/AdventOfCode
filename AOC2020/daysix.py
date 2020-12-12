from typing import List
from collections import Counter
      
def input(path:str)-> List[str]:
    with open(path) as f:
        group = []
        grouplist = []
        for line in f:
            if line == "\n":
                grouplist.append(group)
                group = []
            else:
                group.append(line.strip("\n"))
        grouplist.append(group)

        print(grouplist)
        return grouplist

def count_votes(grouplist:List[str])->int:
    count = 0
    for group in grouplist:
        x =  len(set([_list for y in group for _list in y]))
        count += x
    return count

def count_yes(grouplist:List[str])->int:
    count = 0
    for group in grouplist:
        group_length = len(group)
        count_dict =  Counter([_list for y in group for _list in y])
        
        if group_length in count_dict.values():
            count += sum([1 if val==group_length else 0 for val in count_dict.values()])
        
    return count

if __name__ == "__main__":

    # test one
    testline= [
                ["abc"],
                ['a','b','c'],
                ['ab','ac'],
                ['a','a','a','a'],
                ['b']
                ]         
    test_count = count_votes(testline)
    print(test_count)
    assert test_count == 11

    grouplist = input("/Users/blabaschin/Documents/Technical/GitHub/AOC2020/daysix.txt")

    # part one

    print("Vote Count:", count_votes(grouplist))

    # test two

    test_count = count_yes(testline)
    assert test_count == 6

    # part two
    print("Yes Count:", count_yes(grouplist))