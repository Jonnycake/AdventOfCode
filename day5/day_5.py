#!/usr/bin/env python

def convertInfo(specifier):
    row_num = 0
    exp = 6
    for char in specifier[0:7]:
        if char == 'B':
            row_num += 2**exp
        exp -= 1

    col_num = 0
    exp = 2
    for char in specifier[7:]:
        if char == 'R':
            col_num += 2**exp
        exp -= 1

    return {
        'row_num': row_num,
        'col_num': col_num,
        'seat_id': row_num * 8 + col_num,
    }

with open("input","r") as f:
    max_seat_id = 0
    min_seat_id = 0
    seat_sum = 0
    for line in f:
        line = line.strip()

        info = convertInfo(line)
        if info['seat_id'] > max_seat_id:
            max_seat_id = info['seat_id']

        if info['seat_id'] < min_seat_id or min_seat_id == 0:
            min_seat_id = info['seat_id']
        seat_sum += info['seat_id']

    max_sum = max_seat_id*(max_seat_id+1)/2
    min_sum = (min_seat_id-1)*(min_seat_id)/2
    my_seat_id = max_sum - min_sum - seat_sum

    print(max_seat_id)
    print(my_seat_id)
