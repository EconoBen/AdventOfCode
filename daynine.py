from typing import List


def input(path:str)-> List[str]:
    with open(path) as f:
        raw = f.read()
    text_list = [int(string) for string in raw.split("\n")]
    return text_list

def iter_list(preamble:int, text_list:List[str]):

    for _ in text_list[:preamble]:
        for pointer2 in text_list[preamble:]:
            diff_options = [pointer2-opt for opt in text_list[:preamble]]
            intersection = [value for value in diff_options if value in text_list[:preamble]] 
            if len(intersection) >= 1:
                # shift both lists right one
                return iter_list(preamble, text_list[1:])
            else:
                # if nothing is there return pointer 2 as answer
                return pointer2

def contiguous_number(missing_number:int, text_list:List[str])->List[int]:
    contiguous_list = []
    for pointer1 in text_list[:len(text_list)-1]:
        contiguous_list.append(pointer1)
        for pointer2 in text_list[1:]:
            contiguous_list.append(pointer2)
            if sum(contiguous_list) < missing_number:
                continue
            elif sum(contiguous_list) > missing_number:
                return contiguous_number(missing_number, text_list[1:])
            else:
                return contiguous_list
    

def parse_list(preamble:int, text_list:List[str])->List[int]:
   
    missing_number = iter_list(preamble, text_list)
    contiguous_list = contiguous_number(missing_number, text_list)
    return [missing_number,contiguous_list]

if __name__ == "__main__":

    # test text
    test_text = input('/Users/blabaschin/Documents/Technical/GitHub/AOC2020/dayninetest.txt')


    # test one
    test_result = parse_list(5,test_text)
    assert test_result[0] == 127
    print("test one:", test_result[0])

    # part one    
    text = input('/Users/blabaschin/Documents/Technical/GitHub/AOC2020/daynine.txt')

    results = parse_list(25, text)
    print("part one:", results[0])

    # test two 

    assert test_result[1] == [15,25,47,40]
    print("test two:", test_result[1])

    # part two 
    print("part two:", min(results[1])+ max(results[1]))
