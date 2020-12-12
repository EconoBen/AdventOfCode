from typing import List, Tuple
import time

def input(path:str)-> List[str]:
    with open(path) as f:
        raw = f.read()
    text_list = raw.split("\n")
    return text_list

def accumulator(acc:int, ind_list:List[int], text_list:List[str], index_tracker:List[int])->int:
    if ind_list in index_tracker:
        index_tracker.remove(ind_list)
        
    elif ind_list not in index_tracker:
        return acc
    
    instruct = text_list[ind_list[0]:ind_list[1]]
    
    key, val = instruct[0].rsplit(" ")
    val = int(val)
    if key == 'acc':
        # add value and continue
        acc += val
        ind_list = [ind_list[0]+1, ind_list[1]+1]
        return accumulator(acc, ind_list, text_list, index_tracker)
    elif key == 'nop':
        # skip
        ind_list = [ind_list[0]+1, ind_list[1]+1]
        return accumulator(acc, ind_list, text_list, index_tracker)
    elif key == 'jmp':
        # jump to different command
        ind_list = [ind_list[0]+val, ind_list[1]+val]
        return accumulator(acc, ind_list, text_list, index_tracker)

def fixed_accumulator(acc:int, ind_list:List[int], text_list:List[str], index_tracker:List[int])->int:
    
    if ind_list in index_tracker:
        index_tracker.remove(ind_list)
    
    elif ind_list not in index_tracker:
        return False

    instruct = text_list[ind_list[0]:ind_list[1]]
    
    key, val = instruct[0].rsplit(" ")
    val = int(val)

    if key == 'acc':
        # add value and continue
        acc += val
        ind_list = [ind_list[0]+1, ind_list[1]+1]
        if text_list[ind_list[0]:ind_list[1]]:
            return fixed_accumulator(acc, ind_list, text_list, index_tracker)
        else:
            return acc
    elif key == 'nop':
        # skip
        ind_list = [ind_list[0]+1, ind_list[1]+1]
        if text_list[ind_list[0]:ind_list[1]]:
            return fixed_accumulator(acc, ind_list, text_list, index_tracker)
        else:
            return acc
    elif key == 'jmp':
        # jump to different command
        if val != 0:
            ind_list = [ind_list[0]+val, ind_list[1]+val]
        else:
            ind_list = [ind_list[0]+1, ind_list[1]+1]

        if text_list[ind_list[0]:ind_list[1]]:
            return fixed_accumulator(acc, ind_list, text_list, index_tracker)
        else:
            return acc

def run_accumulator(text_list:List[str]):
   
    acc = 0
    ind_list = [0,1]
    index_tracker = [[x, x+1] for x in range(len(text_list))]
    accumulator_val = accumulator(acc, ind_list, text_list, index_tracker)
    return accumulator_val
       
def fixed_run(text_list:List[str]):

    acc = 0
    ind_list = [0,1]
    index_tracker = [[x, x+1] for x in range(len(text_list))]
    intruct_lists = []
    # create a new list for each jmp and nop in the list. if it repeats an instruction, return and replace with new list
    for index, string in enumerate(text_list):
        temp = text_list.copy()
        if "nop" in temp[index]:
            temp[index] = temp[index].replace("nop", "jmp")
            intruct_lists.append(temp)
        elif "jmp" in temp[index]:
            temp[index] = temp[index].replace("jmp", "nop")
            intruct_lists.append(temp)

    for _list in intruct_lists:
        temp_tracker = index_tracker.copy()
        temp_ind_list = ind_list.copy()
        temp_acc = acc
        result = fixed_accumulator(temp_acc, temp_ind_list, _list, temp_tracker)
        if result == False:
            continue
        else:
            return result
    

if __name__ == "__main__":
    
    # test text
    test_text = input('/Users/blabaschin/Documents/Technical/GitHub/AOC2020/dayeighttest.txt')

    # test one
    assert run_accumulator(test_text) == 5

    # part one    
    text = input('/Users/blabaschin/Documents/Technical/GitHub/AOC2020/dayeight.txt')
    
    val = run_accumulator(text)
    print(val)

    # test two 

    fixed_val = fixed_run(test_text)
    print(fixed_val)

    # part two 
    true_val = fixed_run(text)
    print(true_val)


    