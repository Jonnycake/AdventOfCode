#!/usr/bin/env python

with open('input', 'r') as f:
    complements = {}
    for line in f:
        num = int(line)
        complement = 2020-num

        if complement in complements.keys():
            print (num * complement)
            break

        complements[num] = 2020 - num
