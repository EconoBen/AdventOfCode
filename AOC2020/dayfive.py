import numpy as np
from typing import List, Tuple



def binary_seats(seatstring:str, row:List[int], col:List[int])->Tuple[int, int]:
    
    if len(seatstring) == 1:
        if seatstring[0] == "R":
            col = col[len(col)//2:][0]
            return (row[0], col, row[0] * 8 + col)
        elif seatstring[0] == "L":
            col = col[:len(col)//2][0]
            return (row[0], col, row[0] * 8 + col)
    elif seatstring[0] == "F":
        row = row[:len(row)//2]
        return binary_seats(seatstring[1:], row, col)
    elif seatstring[0] == "B":
        row = row[len(row)//2:]
        return binary_seats(seatstring[1:], row, col)
    elif seatstring[0] == "R" and len(seatstring) != 1:
        col = col[len(col)//2:]
        return binary_seats(seatstring[1:], row, col)
    elif seatstring[0] == "L" and len(seatstring) != 1:
        col = col[:len(col)//2]
        return binary_seats(seatstring[1:], row, col)

    

if __name__ == "__main__":

    testcases = ['BFFFBBFRRR','FFFBBBFRRR','BBFFBBFRLL']

    seat_list = []
    counter = 0
    row_counter = [x for x in range(0,128)]
    col_counter = [y for y in range(0, 8)]

    # test part one
    while counter < len(testcases):
        seat = binary_seats(testcases[counter], row_counter, col_counter)
        print("seat:", seat[0:2], "product",seat[-1] )
        seat_list.append(seat)
        counter += 1
    
    # part one

    seat_list = []
    counter = 0
    row_counter = [x for x in range(0,128)]
    col_counter = [y for y in range(0, 8)]
 
    with open("/Users/blabaschin/Documents/Technical/GitHub/AOC2020/dayfive.txt") as f:
        file = [line.replace("\n", "") for line in f.readlines()]

    while counter < len(file):
        seat = binary_seats(file[counter], row_counter, col_counter)
        seat_list.append(seat[-1])
        counter += 1

    # part two
 
    with open("/Users/blabaschin/Documents/Technical/GitHub/AOC2020/dayfive.txt") as f:
        file = [line.replace("\n", "") for line in f.readlines()]

    taken_seats = []
    counter = 0
    row_counter = [x for x in range(0,128)]
    col_counter = [y for y in range(0, 8)]

    while counter < len(file):
        seat = binary_seats(file[counter], row_counter, col_counter)
        taken_seats.append(seat[2])
        counter += 1

    taken_seats = sorted(taken_seats)
    my_nbrs = [
        (taken_seats[i], taken_seats[i + 1])
        for i in range(len(taken_seats) - 1)
        if taken_seats[i + 1] - taken_seats[i] > 1
    ]
    print(f"max_seat: {taken_seats[-1]}")
    print(f"my_seat: {my_nbrs[0][0] + 1}")

