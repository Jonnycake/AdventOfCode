#!/usr/bin/env python

with open("input", "r") as f:
    num_valid_part_1 = 0
    num_valid_part_2 = 0
    for line in f:
        count_range, line = line.split(" ", 1)
        char, passwd = line.split(": ", 1)

        # Part 1
        count = passwd.count(char)
        min, max = [int(x) for x in count_range.split("-")]
        if count >= min and count <= max:
            num_valid_part_1 += 1

        # Part 2
        length = len(passwd)
        is_valid = False
        is_valid ^= length >= min and passwd[min - 1] == char
        is_valid ^= length >= max and passwd[max - 1] == char
        if is_valid:
            num_valid_part_2 += 1

    print("Part 1: %d" % (num_valid_part_1))
    print("Part 1: %d" % (num_valid_part_2))
